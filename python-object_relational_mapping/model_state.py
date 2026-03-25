#!/usr/bin/python3
"""Contains the class definition of a State and Base."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class State linked to MySQL table states."""
    __tablename__ = \x27states\x27
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
