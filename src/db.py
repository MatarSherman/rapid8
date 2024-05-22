from pymongo import MongoClient

_mongo_client = None


def init_mongo_client():
    global _mongo_client
    if not _mongo_client:
        _mongo_client = MongoClient(
            "mongodb+srv://matar:matar@rapid-cluster.ykvrnni.mongodb.net/"
            "?retryWrites=true&w=majority&appName=rapid-cluster"
        )


def close_mongo_client():
    _mongo_client.close()


def get_mongo_client():
    global _mongo_client
    if not _mongo_client:
        init_mongo_client()
    return _mongo_client
