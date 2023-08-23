"""
class definition of a State and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, string
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class state(Base):
    #contains the table to be mapped to, and names datatypes of columns in it
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
        autoincrement = True, unique = True, nullable = False)
    name = Column(String(128), nullable = False)