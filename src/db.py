from pymongo import MongoClient

from src.config import get_settings

_mongo_client = None


def init_mongo_client():
    global _mongo_client
    if not _mongo_client:
        _mongo_client = MongoClient(get_settings().CONNECTION_STRING)


def close_mongo_client():
    _mongo_client.close()


def get_mongo_client():
    global _mongo_client
    if not _mongo_client:
        init_mongo_client()
    return _mongo_client
