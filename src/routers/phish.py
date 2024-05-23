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
async def get_report(start: datetime, end: datetime = None) -> dict[str, Any]:
    if not end:
        end = datetime.now(timezone.utc)

    query = {"submission_time": {"$gte": start, "$lt": end}}
    cursor = phish_collection.find(query, projection={"_id": 0, "url": 1})

    urls = set([document["url"] async for document in cursor])
    return {
        "urls": urls,
        "count": len(urls),
        "tlds": get_sorted_tlds_amounts(urls),
    }


@router.get("/details")
async def get_phish_details(domain_name: str) -> list[str]:
    if not domain(domain_name):
        raise HTTPException(
            status_code=400,
            detail="Invalid domain format. Please enter a valid domain name.",
        )

    query = {"url": {"$regex": f"^(http|https)://{domain_name}(/.*)*$"}}

    query_result = phish_collection.find(
        query, projection={"_id": 0, "phish_detail_url": 1}
    )

    return [document["phish_detail_url"] async for document in query_result]
