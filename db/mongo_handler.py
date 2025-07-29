from pymongo import MongoClient
from datetime import datetime
import logging

client = MongoClient("mongodb+srv://becoder123:Jexy098@data.mf41ozl.mongodb.net/?retryWrites=true&w=majority&appName=Data")
db = client["grocery_scraper"]
collection = db["products"]

def upsert_product(product_data):
    product_id = product_data["product_id"]
    price_entry = {
        "date": datetime.utcnow(),
        "price": product_data["price"]
    }

    collection.update_one(
        {"product_id": product_id},
        {
            "$set": {
                "name": product_data["name"],
                "category": product_data["category"],
                "brand": product_data["brand"],
                "quantity": product_data["quantity"],
                "image_url": product_data["image_url"],
                "last_updated": product_data["last_updated"]
            },
            "$push": {"price_history": price_entry},
            "$setOnInsert": {"rating": product_data["rating"]}
        },
        upsert=True
    )
