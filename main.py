import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import random, json, logging
from utils.logger import setup_logger
from Scraper.zepto_scraper import scrape_category


CATEGORIES = {
   "atta_rice_oil_dals": "atta-rice-oil-dals/atta-rice-oil-dals/cid/2f7190d0-7c40-458b-b450-9a1006db3d95/scid/84f270cf-ae95-4d61-a556-b35b563fb947",
    "dairy-bread-eggs": "dairy-bread-eggs/dairy-bread-eggs/cid/4b938e02-7bde-4479-bc0a-2b54cb6bd5f5/scid/f594b28a-4775-48ac-8840-b9030229ff87",
    "fruits_vegetables": "fruits-vegetables/fresh-vegetables/cid/64374cfe-d06f-4a01-898e-c07c46462c36/scid/b4827798-fcb6-4520-ba5b-0f2bd9bd7208",
    "meats-fish-eggs": "meats-fish-eggs/meats-fish-eggs/cid/4654bd8a-fb30-4ee1-ab30-4bf581b6c6e3/scid/b6fbf886-79f1-4a34-84bf-4aed50175418",
    "atta-rice-oil-dals":"atta-rice-oil-dals/oil/cid/2f7190d0-7c40-458b-b450-9a1006db3d95/scid/2b5e863c-9497-46ae-a7e9-85f6ef7380da",
    "atta-rice-oil-dals": "atta-rice-oil-dals/ghee/cid/2f7190d0-7c40-458b-b450-9a1006db3d95/scid/56c015a7-b283-4e7a-b3ba-0f76f4f181dc",
    "masala-dry-fruits-more":"masala-dry-fruits-more/masala-dry-fruits-more/cid/0c2ccf87-e32c-4438-9560-8d9488fc73e0/scid/8b44cef2-1bab-407e-aadd-29254e6778fa",
    "munchies":"munchies/munchies/cid/d2c2a144-43cd-43e5-b308-92628fa68596/scid/d648ea7c-18f0-4178-a202-4751811b086b",
    "packaged-food":"packaged-food/packaged-food/cid/5736ad99-f589-4d58-a24b-a12222320a37/scid/dbb39a86-256b-4664-81ed-6668418a5436",
    "biscuits":"biscuits/biscuits/cid/2552acf2-2f77-4714-adc8-e505de3985db/scid/3a10723e-ba14-4e5c-bdeb-a4dce2c1bec4",
    "breakfast-sauces":"breakfast-sauces/breakfast-sauces/cid/f804bccc-c565-4879-b6ab-1b964bb1ed41/scid/68922181-4e0e-4a6b-9862-cf1a02ba240e", 
    "cold-drinks-juices":"cold-drinks-juices/cold-drinks-juices/cid/947a72ae-b371-45cb-ad3a-778c05b64399/scid/7dceec53-78f9-4f06-83d7-c8edd9c2f71a"
}

setup_logger()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def run_scraper():
    all_products = []
    for name, url in CATEGORIES.items():
        logging.info(f"Scraping category: {name}")
        data = scrape_category(driver, name, url)
        all_products.extend(data)
        logging.info(f"Scraped {len(data)} items from {name}")
        time.sleep(random.randint(60, 90))
    return all_products

if __name__ == "__main__":
    all_data = run_scraper()
    logging.info(f"Total scraped products: {len(all_data)}")
    print(json.dumps(all_data[:5], indent=4, default=str))
    driver.quit()
