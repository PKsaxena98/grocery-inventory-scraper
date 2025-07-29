# 🛒 Grocery Inventory Scraper (Zepto)

A Python-based scraper that collects grocery product data from Zepto.com and stores it in MongoDB. The scraper supports scrolling, price history tracking, and category-wise scraping.

---

##  Features

- Dynamic scroll scraping with Selenium
- Product upsert in MongoDB (no duplication)
- Price history tracking
- Modular code with `scraper/`, `db/`, and `utils/`
- Configurable categories

---

## ⚙ Setup Instructions

## 🧾 MongoDB Schema Overview

{
  "product_id": "aashirvaad_atta_5kg",
  "name": "Aashirvaad Atta",
  "category": "atta_rice_oil_dals",
  "brand": "Aashirvaad",
  "price": {
    "original": 250.0,
    "discounted": 240.0
  },
  "quantity": "5 kg",
  "rating": null,
  "image_url": "https://cdn.zepto.com/products/image.jpg",
  "last_updated": "2025-07-29T18:45:00Z",
  "price_history": [
    {
      "date": "2025-07-27T18:00:00Z",
      "price": {
        "original": 260.0,
        "discounted": 240.0
      }
    }
  ]
}

## Example Output 

_id: "68853a895e95d47153f526a9"
product_id :"vijay_ragi_flour_unknown_unknown"
brand: "Unknown"
category:"atta_rice_oil_dals"
image_url:"https://cdn.zeptonow.com/production/tr:w-1280,ar-2400-2400,pr-true,f-a…"
last_updated:"2025-07-26T20:23:30.634+00:00"
name:"Vijay Ragi Flour"
price_history:0
Object:
date:
"2025-07-26T20:23:30.634+00:00"
price:
 Object:
  original:85
  discounted: 85
quantity :"Unknown"
rating: null

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/grocery-inventory-scraper.git
cd grocery-inventory-scraper
