#!/usr/bin/python3
"""
Start link class to table in database
"""
import sys

from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(bind=engine)
    new_mexico = session.query(State).filter_by(id=2).first()
    new_mexico.name = "New Mexico"
    session.commit()
    session.close()
