#!/usr/bin/python3
"""
Script to add the `State` object `Louisiana` to the
database 'hbtn_0e_6_usa'
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    # establish connection to the mysql server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    # create State object/ instace
    new_state = State(name='Louisiana')

    # add new State object to our database
    session.add(new_state)

    # print id of new State object
    state = session.query(State).filter_by(name='Louisiana')
    print(state.id)
