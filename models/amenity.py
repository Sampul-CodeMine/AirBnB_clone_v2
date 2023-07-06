#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Represents an Amenity for a MySQL database.
    Inherits from SQLAlchemy Base and links to the MySQL table amenities.
    Attributes:
    tablename: amenities
        name: input name
        place_amenities: place-amenity relationship
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)
