#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """This class defines a user by various attributes
    Represents a user for a MySQL database.
    Inherits from SQLAlchemy Base and links to the MySQL table users.
    Attributes:
        tablename: users
        email: email address
        password: password for the login
        first_name: first name
        last_name: last name
        places: place-user replationship
        reviews: user-review relationship
    """
    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")
