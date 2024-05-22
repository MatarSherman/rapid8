from datetime import datetime, timezone
from typing import Any
from fastapi import APIRouter, HTTPException
from validators import domain

from src.db import get_mongo_client
from src.utils import get_sorted_tlds_amounts


router = APIRouter(prefix="/phish")
mongo_client = get_mongo_client()
phish_collection = mongo_client["Rapid"]["phishing-data"]


@router.get("/report")
def get_report(start: datetime, end: datetime = None) -> dict[str, Any]:
    if not end:
        end = datetime.now(timezone.utc)

    pipeline = [
        {"$match": {"submission_time": {"$gte": start, "$lt": end}}},
        {
            "$group": {
                "_id": None,
                "urls": {"$addToSet": "$url"},
                "total_count": {"$sum": 1},
            }
        },
        {"$project": {"_id": 0, "urls": 1, "total_count": 1}},
    ]
    aggregationResult = phish_collection.aggregate(pipeline)

    report = next(aggregationResult, {"urls": [], "count": 0})
    report["tlds"] = get_sorted_tlds_amounts(report["urls"])
    return report


@router.get("/details")
def get_phish_details(domain_name: str) -> list[str]:
    if not domain(domain_name):
        raise HTTPException(
            status_code=400,
            detail="Invalid domain format. Please enter a valid domain name.",
        )

    query = {
        "url": {
            "$regex": f"^https?://(?:([^.]+\\.)*)?({domain_name})(?:/.*)?$",
            "$options": "i",
        }
    }

    query_result = phish_collection.find(
        query, projection={"_id": 0, "phish_detail_url": 1}
    )

    return [document["phish_detail_url"] for document in query_result]
