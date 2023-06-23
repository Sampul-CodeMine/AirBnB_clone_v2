#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from os import getenv
from sqlalchemy import Column, String
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
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', cascade='all, delete', backref='state')
    else:
        @property
        def cities(self) -> list:
            """Special method getter method to get the cities
            Return:
                list of cities with state_id = self.id
            """
            from models import storage
            from models.city import City
            list_cities = []
            dict_cities = storage.all(City)
            for city in dict_cities.values():
                if city.state_id == self.id:
                    list_cities.append(city)
            return (list_cities)
