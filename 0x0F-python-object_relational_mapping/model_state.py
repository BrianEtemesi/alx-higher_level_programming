#!/usr/bin/python3
"""
Defines a class `State` and an instance `Base = declarative_base():`
Connects to a MySQL server running on `localhost`
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# create a declarative base instance
Base = declarative_base()


class State(Base):
    """
    class represantation of a state
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
