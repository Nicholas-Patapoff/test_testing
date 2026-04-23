import os


class Config:
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///app.db")
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
    MAX_PAGE_SIZE = int(os.getenv("MAX_PAGE_SIZE", "100"))
