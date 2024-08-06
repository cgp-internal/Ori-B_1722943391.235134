from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class ExampleModel(Base):
    __tablename__ = 'examples'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)