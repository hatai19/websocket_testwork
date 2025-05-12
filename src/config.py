import os
from dotenv import load_dotenv

load_dotenv()

db_user = os.getenv("POSTGRES_USER")
db_host = os.getenv("POSTGRES_HOST")
db_password = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")
db_port = os.getenv("POSTGRES_PORT")

postgres_url = f"postgresql+asyncpg://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"