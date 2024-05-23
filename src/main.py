from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from dotenv import load_dotenv

from src.db import close_mongo_client, init_mongo_client
from src.scheduler import schedule_update_db
from .routers import phish

load_dotenv()

app = FastAPI()


def on_startup():
    init_mongo_client()
    schedule_update_db()


app.add_event_handler("startup", on_startup)
app.add_event_handler("shutdown", close_mongo_client)

app.include_router(phish.router)


@app.get("/")
def get_root():
    return RedirectResponse(url="/docs", status_code=307)
