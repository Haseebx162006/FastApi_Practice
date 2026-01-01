import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

db_url = os.getenv("DATABASE_URL")

if not db_url:
    raise RuntimeError("DATABASE_URL is not set. Check your .env file location.")

engine = create_engine(db_url)

session = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)
