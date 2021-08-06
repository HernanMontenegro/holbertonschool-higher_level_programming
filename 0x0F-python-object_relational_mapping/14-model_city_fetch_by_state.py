#!/usr/bin/python3
''' 7 - Module '''

from sys import argv as av
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
import sqlalchemy as db
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = db.create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                              .format(av[1], av[2], av[3]), pool_pre_ping=True)
    Session = sessionmaker()
    Session.configure(bind=engine)

    session = Session()

    for row in session.query(City, State).join(State).order_by(City.id):
        print(row[1].name + ": " + "(" + str(row[0].id) + ") " + row[0].name)
