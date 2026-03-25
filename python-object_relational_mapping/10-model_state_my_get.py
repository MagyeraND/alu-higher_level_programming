#!/usr/bin/python3
"""Prints State id matching name passed as argument."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(\x27mysql+mysqldb://{}:{}@localhost/{}\x27.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name == sys.argv[4]).first()
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
