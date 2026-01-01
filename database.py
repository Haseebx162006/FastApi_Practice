from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url= "postgresql://postgres:Python1600@localhost:5432/mydb"
engine= create_engine(db_url)

session= sessionmaker(autoflush=False, bind= engine, autocommit=False)