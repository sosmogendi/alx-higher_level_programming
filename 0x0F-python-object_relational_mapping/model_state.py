#!/usr/bin/python3
"""
Define the State class and create a mapping to the states table in the database.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    Define the State class to represent the states table in the database.
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        """
        Initialize a new State object with a given name.
        """
        self.name = name
