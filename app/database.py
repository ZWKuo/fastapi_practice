from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import setting


SQLALCHEMY_DATABASE_URL = f"postgresql://{setting.database_user}:{setting.database_password}@{setting.database_url}:{setting.database_port}/{setting.database_name}"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()