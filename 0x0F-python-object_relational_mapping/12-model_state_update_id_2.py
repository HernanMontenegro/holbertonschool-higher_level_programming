#!/usr/bin/python3
''' 10 - Module '''

from sys import argv as av
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
import sqlalchemy as db
from sqlalchemy.sql.expression import text
from model_state import Base, State


if __name__ == "__main__":
    engine = db.create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                              .format(av[1], av[2], av[3]), pool_pre_ping=True)
    Session = sessionmaker()
    Session.configure(bind=engine)

    session = Session()

    Louisiana = State(name="New Mexico")
    session.add(Louisiana)

    session.query(State).filter(State.id == 2).update({'name': "New Mexico"})
    session.commit()
