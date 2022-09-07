from sqlalchemy import Column, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Integer, Text

Base = declarative_base(metadata=MetaData(schema="pet"))


class Pet(Base):
    __tablename__ = "petstore"

    __table_args__ = {'schema': 'pet'}

    petname = Column(Text, nullable=True)
    id = Column(Integer, nullable=False, primary_key=True)
    catagory = Column(Text, nullable=True)
    status = Column(Text, nullable=True)

    def dict(self):
        return {
            "petname": self.petname,
            "id": self.id,
            "catagory": self.catagory,
            "status": self.status,
        }
