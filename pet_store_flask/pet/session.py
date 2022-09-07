from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# db_path = os.path.join(BASE_DIR, "petstore.db")
# print(db_path)
# print(os.getenv(db_path))

engine = create_engine('postgresql://postgres:admin@localhost:5432/petdata', echo=True)
# connect_args={'check_same_thread': False}

Session = sessionmaker(bind=engine)
session = Session()