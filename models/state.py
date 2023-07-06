#!/usr/bin/python3
""" State Module for HBNB project """
import models
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship

"""
This is a Python class that models a State class but inherits from the
BaseModel class as the Parent Class
"""


class State(BaseModel, Base):
    """
    This is a class modelling the State object for AirBnB Clone project.
    Represents a state for a MySQL database.
    Inherits from SQLAlchemy Base and links to the MySQL table states.

    Attributes:
        tablename: states
        name (str): the name of the State
        city (str): city-state replationship
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all related City objects."""
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
