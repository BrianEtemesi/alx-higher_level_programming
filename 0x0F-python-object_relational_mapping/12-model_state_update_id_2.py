#!/usr/bin/python3
"""
script to change name of a `State` object from
the database 'hbtn_0e_6_usa'
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    # establish connection to the mysq server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    """ change the name of the State where id = 2 to New Mexico"""

    state = session.query(State).filter_by(id=2).first()
    state.name = 'New Mexico'
    session.commit()
