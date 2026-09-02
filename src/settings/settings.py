import os
from pathlib import Path
from dotenv import load_dotenv

# Subindo 3 níveis para achar o .env na raiz (settings/ -> src/ -> raiz)
RAIZ_PROJETO = Path(__file__).resolve().parents[2]
load_dotenv(RAIZ_PROJETO / ".env")

class Settings:
    def __init__(self):
        self.db_host: str | None = os.getenv("DB_HOST")
        self.db_name: str | None = os.getenv("DB_NAME")
        self.db_port: int = int(os.getenv("DB_PORT", "3306"))
        self.db_user: str | None = os.getenv("DB_USER")
        self.db_pass: str | None = os.getenv("DB_PASS")
        self.app_host: str | None = os.getenv("APP_HOST")
        self.app_port: int = int(os.getenv("APP_PORT", "8000"))

configuracoes = Settings()

