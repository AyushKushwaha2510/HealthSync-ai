from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from dotenv import load_dotenv

from app.core.config import settings

load_dotenv()

engine = create_engine(
    settings.DATABASE_URL,
    echo=True,          # prints SQL queries
    pool_pre_ping=True  # checks dead connections
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()