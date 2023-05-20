#!/usr/bin/python3
"""
prints all `City` objects from the database `hbtn_0e_14_usa`
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

if __name__ == '__main__':

    # establish connection to the mysql database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    State.cities = relationship("City", order_by=City.id,
                                back_populates="state")

    # query table
    for city in session.query(City).order_by(City.id).all():
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))
