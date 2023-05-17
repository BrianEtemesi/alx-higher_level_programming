#!/usr/bin/python3
"""
lists all `State` objects that contain the letter a from the
database `hbtn_0e_6_usa`
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    # establish connection with the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    # query table
    states = session.query(State)
    s_with_a = states.filter(State.name.like('%a%')).order_by(State.id).all()

    # print results
    for state in s_with_a:
        print("{}: {}".format(state.id, state.name))
