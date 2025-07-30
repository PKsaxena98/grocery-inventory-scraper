from pymongo import MongoClient
from datetime import datetime
import logging
from dotenv import load_dotenv
import os

load_dotenv() 

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

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
