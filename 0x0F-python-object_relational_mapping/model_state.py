#!/usr/bin/python3
''' model_state - module '''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    ''' State table class '''

    __tablename__ = 'states'

    id = Column(Integer, autoincrement=1, primary_key=True)
    name = Column(String(128), nullable=False)
