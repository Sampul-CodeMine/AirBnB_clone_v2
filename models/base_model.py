#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import models
import uuid as uid
from datetime import datetime as dt
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String

"""
This is a Python class that will be the Base class or Parent class from which
all other classes will inherit from.
"""

Base = declarative_base()


class BaseModel:
    """
    This is a class modelling the BaseModel object for AirBnB Clone project.
    """
    """ creating class properties """
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=dt.utcnow())
    updated_at = Column(DateTime, nullable=False, default=dt.utcnow())

    def __init__(self, *args, **kwargs) -> None:
        """This is the constructor for the BaseModel class that instantiates
        an instance of the BaseModel object when created.

        Args:
            args (any) - non-keyworded arguments
            kwargs (any) - keyworded key and valued paired arguments
        """
        self.id = str(uid.uuid4())
        self.created_at = self.updated_at = dt.utcnow()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = dt.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

    def __str__(self) -> dict:
        """Public instance method for the BaseModel that returns a String
        Representation of our BaseModel class"""
        d = self.__dict__.copy()
        d.pop("_sa_instance_state", None)
        return "[{}] ({}) {}".format(type(self).__name__, self.id, d)

    def __repr__(self) -> dict:
        """return a string representaion
        """
        return self.__str__()

    def save(self) -> None:
        """Public instance method that updates the `updated_at` public
        instance property"""
        self.updated_at = dt.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self) -> dict:
        """Public instance method that returns a dictionary of key/values of
        __dict__ of the BaseModel instance"""
        data = self.__dict__.copy()
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict.pop("_sa_instance_state", None)
        return my_dict

    def delete(self) -> None:
        """Public instance method that Delete current instance from storage
        """
        models.storage.delete(self)
