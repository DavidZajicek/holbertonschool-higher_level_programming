#!/usr/bin/python3
"""
0. Get all states
mandatory
Write a script that lists all states from the database hbtn_0e_0_usa:
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State based classism
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    pass
