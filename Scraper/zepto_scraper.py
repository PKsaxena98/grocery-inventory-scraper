from bs4 import BeautifulSoup
import time, random, logging
from utils.helpers import  slow_scroll_to_bottom
from db.mongo_handler import upsert_product
from datetime import datetime, timezone

BASE_URL = "https://www.zeptonow.com/cn/"
CATEGORIES = {
   "atta_rice_oil_dals": "atta-rice-oil-dals/atta-rice-oil-dals/cid/2f7190d0-7c40-458b-b450-9a1006db3d95/scid/84f270cf-ae95-4d61-a556-b35b563fb947",
    "dairy-bread-eggs": "dairy-bread-eggs/dairy-bread-eggs/cid/4b938e02-7bde-4479-bc0a-2b54cb6bd5f5/scid/f594b28a-4775-48ac-8840-b9030229ff87",
    "fruits_vegetables": "fruits-vegetables/fresh-vegetables/cid/64374cfe-d06f-4a01-898e-c07c46462c36/scid/b4827798-fcb6-4520-ba5b-0f2bd9bd7208",
    "meats-fish-eggs": "meats-fish-eggs/meats-fish-eggs/cid/4654bd8a-fb30-4ee1-ab30-4bf581b6c6e3/scid/b6fbf886-79f1-4a34-84bf-4aed50175418",
    "atta-rice-oil-dals":"atta-rice-oil-dals/oil/cid/2f7190d0-7c40-458b-b450-9a1006db3d95/scid/2b5e863c-9497-46ae-a7e9-85f6ef7380da",
    "atta-rice-oil-dals": "atta-rice-oil-dals/ghee/cid/2f7190d0-7c40-458b-b450-9a1006db3d95/scid/56c015a7-b283-4e7a-b3ba-0f76f4f181dc",
    "masala-dry-fruits-more":"masala-dry-fruits-more/masala-dry-fruits-more/cid/0c2ccf87-e32c-4438-9560-8d9488fc73e0/scid/8b44cef2-1bab-407e-aadd-29254e6778fa",
    "munchies":"munchies/cid/d2c2a144-43cd-43e5-b308-92628fa68596/scid/d648ea7c-18f0-4178-a202-4751811b086b",
    "packaged-food":"packaged-food/packaged-food/cid/5736ad99-f589-4d58-a24b-a12222320a37/scid/dbb39a86-256b-4664-81ed-6668418a5436",
    "biscuits":"biscuits/biscuits/cid/2552acf2-2f77-4714-adc8-e505de3985db/scid/3a10723e-ba14-4e5c-bdeb-a4dce2c1bec4",
    "breakfast-sauces":"breakfast-sauces/breakfast-sauces/cid/f804bccc-c565-4879-b6ab-1b964bb1ed41/scid/68922181-4e0e-4a6b-9862-cf1a02ba240e", 
    "cold-drinks-juices":"cold-drinks-juices/cold-drinks-juices/cid/947a72ae-b371-45cb-ad3a-778c05b64399/scid/7dceec53-78f9-4f06-83d7-c8edd9c2f71a"
}

def scrape_category(driver, category_name, category_path):
    full_url = BASE_URL + category_path
    driver.get(full_url)
    slow_scroll_to_bottom(driver)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    products = []

    product_divs = soup.find_all("div", class_="_container_lg_c1j8m_26 _container_c1j8m_3")
    for div in product_divs:
        try:
            name = div.find("div", class_="_base_1i8oq_1 _product-name-container_c1j8m_76").get_text(strip=True)
            price_text = div.find("p", class_="_price_ljyvk_11 _price_lg_ljyvk_26").get_text(strip=True).replace("₹", "")
            discounted_price = float(price_text) if price_text else None
            brand_tag = div.find("p", class_="max-w-fit text-base font-medium text-[#5A6477]")
            brand = brand_tag.get_text(strip=True) if brand_tag else "Unknown"
            quantity_tag = div.find("div", class_="_base_4i17o_1 _pack-size-container_c1j8m_64")
            quantity = quantity_tag.get_text(strip=True) if quantity_tag else "Unknown"
            image_tag = div.find("img")
            image_url = image_tag['src'] if image_tag else None
            
            product_id = f"{name}_{brand}_{quantity}".replace(" ", "_").lower()

            product_data = {
                "product_id": product_id,
                "name": name,
                "category": category_name,
                "brand": brand,
                "price": {
                    "original": discounted_price,
                    "discounted": discounted_price
                },
                "quantity": quantity,
                "rating": None,
                "image_url": image_url,
                "last_updated": datetime.now(timezone.utc)
            }

            upsert_product(product_data)
            products.append(product_data)

        except Exception as e:
            logging.error(f"Error parsing product: {e}")
    return products
