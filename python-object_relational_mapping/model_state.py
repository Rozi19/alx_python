"""
class definition of a State and an instance Base = declarative_base()
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import column, Integer, String


"""declarative_base() callable returns a new base class from 
which all mapped classes should inherit.
connecting with the database and take values from the argument"""

user =sys.argv[1]
passwd = sys.argv[2]
db1 = sys.argv[3]

db = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
    .format(user, passwd, db1), echo = TRUE)
Base = declarative_base()
""" create class state """
class State(Base):
    """ contains the table to be mapped to, and names 
        and datatypes of columns in it."""

    __tablename__ = 'states'
    id = column(Integer, primary_key=True,
        autoincrement = True, unique = True, nullable = False)
    name = column(String(128), nullable = False)

"""
metadata attribute of declarative base class
MetaData.create_all() method is, 
passing in our Engine as a source of database connectivity.
"""
Base.metadata.create_all(db)
