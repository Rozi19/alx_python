"""
class definition of a State and an instance Base = declarative_base()
declarative_base() callable returns a new base class from 
which all mapped classes should inherit.
connecting with the database and take values from the argument"""


from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import column, Integer, String


Base = declarative_base()
class State(Base):
    """ contains the table to be mapped to, and name"""
    __tablename__ = 'states'
    id = column(Integer, primary_key=True,
            autoincrement = True, unique = True, nullable = False)
    name = column(String(128), nullable = False)
Base.metadata.create_all(db)
