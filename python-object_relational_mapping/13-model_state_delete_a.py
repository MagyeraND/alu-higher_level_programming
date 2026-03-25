#!/usr/bin/python3
"""Deletes all State objects with name containing letter a."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(\x27mysql+mysqldb://{}:{}@localhost/{}\x27.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.like(\x27%a%\x27)).all()
    for state in states:
        session.delete(state)
    session.commit()
