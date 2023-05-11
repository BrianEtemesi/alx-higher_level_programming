#!/usr/bin/python3
"""
script to fetch the first `State` object from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    # create engine to connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    # query all states
    query = session.query(State)
    state = query.first()

    if state:
        print("{}: {}".format(state.id, state.name))
