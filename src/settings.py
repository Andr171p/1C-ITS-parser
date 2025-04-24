import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


BASE_DIR = Path(__file__).resolve().parent.parent

ENV_PATH = BASE_DIR / ".env"

load_dotenv(ENV_PATH)


class PostgresSettings(BaseSettings):
    ...


class ITSSettings(BaseSettings):
    login: str = os.getenv("ITS_LOGIN")
    password: str = os.getenv("ITS_PASSWORD")


class Settings(BaseSettings):
    its: ITSSettings = ITSSettings()


settings = Settings()
