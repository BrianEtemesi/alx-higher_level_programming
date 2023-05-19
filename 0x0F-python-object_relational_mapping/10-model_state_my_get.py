#!/usr/bin/python3
"""
prints the `State` object with the name passed as argument from the
database hbtn_0e_6_usa
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

    # query table
    state_name = argv[4]
    state = session.query(State).filter(State.name == '%s' % (state_name,)).first()
    
    if state:
        print(state.id)
    else:
        print('Not found')
