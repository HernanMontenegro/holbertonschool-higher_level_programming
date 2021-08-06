#!/usr/bin/python3
''' 7 - Module '''

from sys import argv as av
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
import sqlalchemy as db
from model_state import Base, State


if __name__ == "__main__":
    engine = db.create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                              .format(av[1], av[2], av[3]), pool_pre_ping=True)
    Session = sessionmaker()
    Session.configure(bind=engine)

    session = Session()

    for instance in session.query(State).order_by(State.id):
        print(instance.id, instance.name)
