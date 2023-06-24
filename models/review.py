#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ Review classto store review information
    Represents a review for a MySQL database.
    Inherits from SQLAlchemy Base and links to the MySQL table reviews.
    Attributes:
        tablename (str): reviews
        text (str): review description.
        place_id (str): The review's place id.
        user_id (str): The review's user id.
    """
    __tablename__ = "reviews"

    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)
