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

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/grocery-inventory-scraper.git
cd grocery-inventory-scraper
