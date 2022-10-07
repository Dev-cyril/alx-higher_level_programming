#!/usr/bin/python3
""" a python file that contains the class definition of a City and 
    an instance Base = declarative_base()
"""

from sys import argv
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """A class that inherits from the decarative base"""
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
