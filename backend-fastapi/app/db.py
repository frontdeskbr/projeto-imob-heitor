from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

import os
DATABASE_URL = os.getenv("DATABASE_URL","postgresql+psycopg2://imob:imob123@localhost:5432/imob")

engine = create_engine(DATABASE_URL, future=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, future=True)
Base = declarative_base()
