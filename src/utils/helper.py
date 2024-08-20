import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_WH_TELCO = os.getenv("DB_WH_TELCO")


def init_engine():
    """
    Function for connect to the database warehouse
    """
    telco_conn = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5434/telco")

    return telco_conn
