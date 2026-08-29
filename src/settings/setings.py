
import os
from pathlib import Path
from dotenv import load_dotenv


RAIZ_PROJETO = Path(__file__).resolve().parents[1]

load_dotenv(RAIZ_PROJETO / ".env")

class Settigs:
    def __init__(self):
        self.db_host = os.getenv("DB_HOST")
        self.db_name = os.getenv("DB_NAME")
        self.db_port = os.getenv("DB_PORT")
        self.db_user = os.getenv("DB_USER")
        self.db_pass = os.getenv("DB_PASS")

        self.app_host = os.getenv("APP_HOST")
        self.app_port = os.getenv("APP_PORT")


configuracoes = Settigs()
