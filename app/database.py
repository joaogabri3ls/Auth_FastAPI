from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()


engine = create_engine(os.getenv('DB_URL'))
Session = sessionmaker(bind=engine)
Base = declarative_base()
