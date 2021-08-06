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

    rows = session.query(State).filter(text(
        "states.name = ('{}')".format(av[4]))
        ).order_by(State.id).all()

    if (len(rows) == 0):
        print("Not found")
    else:
        print(rows[0].id)
