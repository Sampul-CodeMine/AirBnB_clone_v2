#!/usr/bin/python3
"""Importing some Standard modules and modules from our packages"""
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

"""
This is a Python class that models a City class but inherits from the BaseModel
class as the Parent Class
"""


class City(BaseModel, Base):
    """
    This is a class modelling the City object for AirBnB Clone project.
    It inherits BaseModel and Base as Parent Classes

    Attributes:
        places (sqlalchemy relationship): The user-Place relationship.
        state_id (str): the id of the State where the city is
        name (str): the name of the city
    """

    __tablename__ = "cities"

    if getenv('HBNB_TYPE_STORAGE' == 'db'):
        name = Column("name", String(128), nullable=False)
        state_id = Column("state_id", String(60), ForeignKey("states.id"),
                          nullable=False)
        places = relationship('Place', backref='cities', cascade='delete')
    else:
        state_id = ''
        name = ''
