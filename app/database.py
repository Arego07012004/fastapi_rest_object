from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base  # импортируем Base из models.py

DATABASE_URL = "postgresql://areg:7125@127.0.0.1:5432/harward_university"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

