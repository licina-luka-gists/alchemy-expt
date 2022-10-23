from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DB_URI = 'sqlite:///./app.db'
SQLALCHEMY_DB_URI = 'postgresql://tester:abcd@localhost:5434/expt'

engine = create_engine(SQLALCHEMY_DB_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
