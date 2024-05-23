
from functools import lru_cache

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    CONNECTION_STRING: str = ''

    class Config:
        env_file = '.env'

@lru_cache
def get_settings() -> Settings:
    return Settings()