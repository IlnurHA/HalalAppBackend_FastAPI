from pydantic_settings import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).parent


class Settings(BaseSettings):
    db_url: str = f"sqlite+aiosqlite:///{BASE_DIR}/db_local/db.sqlite3"
    db_echo: bool = True
    secret_key: str
    algorithm: str = "HS256"


settings = Settings()
