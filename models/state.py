#!/usr/bin/python3
""" State Module for HBNB project """
import models
from os import getenv
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """
    This is a class modelling the State object for AirBnB Clone project.

    Attributes:
        name (str): the name of the State
    """
    __tablename__ = "states"
    name = Column("name", String(128), nullable=False)
    cities = relationship('City', backref="state",
                              cascade="all, delete-orphan")

    if getenv('HBNB_TYPE_STORAGE' != 'db'):
        @property
        def cities(self):
            """Returns the list of `City` instances
            with `state_id` equals to the current
            """

            cities = list()

            for _id, city in models.storage.all(City).items():
                if city.state_id == self.id:
                    cities.append(city)

            return cities
