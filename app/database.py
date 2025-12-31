from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base

DATABASE_URL = "postgresql://areg:7125@5423:5432/harward_university"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

