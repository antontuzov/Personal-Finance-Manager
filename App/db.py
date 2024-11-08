# db.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# PostgreSQL Database URL
SQLALCHEMY_DATABASE_URL = "postgresql://username:password@localhost:5432/yourdatabase"

# Create the SQLAlchemy engine with PostgreSQL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a session local class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for models to inherit
Base = declarative_base()

