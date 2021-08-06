#!/usr/bin/python3
''' 7 - Module '''

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

    for inst in session.query(State).filter(text("states.name LIKE BINARY '%a%'")).order_by(State.id):
        print(str(inst.id) + ": " + inst.name)
