from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str = "sqlite:///.db_local/db.sqlite3"


settings = Settings()
