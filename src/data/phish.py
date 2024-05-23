from datetime import datetime
from pymongo import InsertOne
import requests
import json

from src.db import get_mongo_client


def process_phish_document(document):
    try:
        return {
            "url": document["url"],
            "phish_detail_url": document["phish_detail_url"],
            "submission_time": datetime.fromisoformat(
                document["submission_time"],
            ),
        }
    except Exception:
        return {}


async def update_db():
    try:
        print("Updating database - this may take a while")
        response = requests.get(
            "http://data.phishtank.com/data/online-valid.json",
        )
        response.raise_for_status()
        data = await response.json()
    except Exception:
        print("Failed to retrieve phish dump, using backup")
        with open("phish-dump.json", "r") as file:
            data = json.load(file)
    finally:
        documents = (process_phish_document(doc) for doc in data)

        phish_collection = get_mongo_client().Rapid.phish_data
        await phish_collection.delete_many({})
        await phish_collection.bulk_write(
            [InsertOne(doc) for doc in documents],
            ordered=False,
        )
        print("Database updated successfuly")
