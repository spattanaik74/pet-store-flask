from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:admin@localhost:5432/petdata', echo=True)

Session = sessionmaker(bind=engine)
session = Session()
