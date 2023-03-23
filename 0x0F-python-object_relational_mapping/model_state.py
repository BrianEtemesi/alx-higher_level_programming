#!/usr/bin/python3
"""
Defines a class `State` and an instance `Base = declarative_base():`
Connects to a MySQL server running on `localhost`
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# create engine to connect to MySQL server
# engine = create_engine('mysql://localhost:3306')

# create a declarative base instance
Base = declarative_base()


class State(Base):
    """
    class represantation of a state
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


# add the state class to the registry 'importing'
# Base.registry.register(State)

# create all tables in the MySQL database
# since we only have `State`, it is the only one created in the mysql db
# Base.metadata.create_all(bind=engine)
