#!/usr/bin/python3
""" a python file that contains the class definition of a State and 
    an instance Base = declarative_base()
"""

from sys import argv
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class State(Base):
    """A class that inherits from the decarative base"""
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)