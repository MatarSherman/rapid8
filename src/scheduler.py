from apscheduler.schedulers.asyncio import AsyncIOScheduler

from src.data.phish import update_db


def schedule_update_db():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(update_db, "interval", hours=1)
    scheduler.start()
