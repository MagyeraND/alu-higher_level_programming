#!/usr/bin/python3
"""Contains class definition of City."""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """Class City linked to MySQL table cities."""
    __tablename__ = \x27cities\x27
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(\x27states.id\x27), nullable=False)
