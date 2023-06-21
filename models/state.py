#!/usr/bin/python3
"""Importing some Standard modules and modules from our packages"""
import models
from os import getenv
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

"""
This is a Python class that models a State class but inherits from the
BaseModel class as the Parent Class
"""


class State(BaseModel, Base):
    """
    This is a class modelling the State object for AirBnB Clone project.

    Attributes:
        name (str): the name of the State
    """
    __tablename__ = "states"

    if getenv('HBNB_TYPE_STORAGE' == 'db'):
        name = Column("name", String(128), nullable=False)
        cities = relationship('City', backref="states",
                              cascade="all, delete-orphan")
    else:
        name = ''

        @property
        def cities(self):
            """A list of cities with state_is == current id"""
            cities = list()

            for _id, city in models.storage.all(City).items():
                if city.state_id == self.id:
                    cities.append(city)

            return (cities)
