#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import models
import uuid as uid
from datetime import datetime as dt
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

"""
This is a Python class that will be the Base class or Parent class from which
all other classes will inherit from.
"""

Base = declarative_base()


class BaseModel:
    """
    This is a class modelling the BaseModel object for AirBnB Clone project.

    Attributes:
        id: unique id generated
        created_at: creation date
        updated_at: updated date
    """
    id = Column("id", String(60), primary_key=True, nullable=False)
    created_at = Column("created_at", DateTime, nullable=False,
                        default=dt.utcnow())
    updated_at = Column("updated_at", DateTime, nullable=False,
                        default=dt.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new BaseModel object
        Args:
            args: it won't be used
            kwargs: arguments for the constructor of the BaseModel
        """
        self.id = str(uid.uuid4())
        self.created_at = self.updated_at = dt.utcnow()
        if kwargs != {} and kwargs is not None and bool(kwargs):
            for k, v in kwargs.items():
                if k in ['created_at', 'updated_at']:
                    v = dt.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if k != '__class__':
                    setattr(self, k, v)
                if 'id' not in kwargs:
                    self.id = str(uid.uuid4())
                if 'created_at' not in kwargs:
                    self.created_at = dt.utcnow()
                if 'created_at' in kwargs and 'updated_at' not in kwargs:
                    self.updated_at = self.created_at
                else:
                    self.updated_at = dt.utcnow()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def __repr__(self):
        """return a string representaion"""
        return self.__str__()

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = dt.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Public instance method that returns a dictionary of key/values of
        __dict__ of the BaseModel instance"""
        data = self.__dict__.copy()
        data["__class__"] = type(self).__name__
        data["created_at"] = data["created_at"].isoformat()
        data["updated_at"] = data["updated_at"].isoformat()
        if data["_sa_instance_state"]:
            data.pop("_sa_instance_state")
        return data

    def delete(self):
        """Public instance method that Deletes the current instance from the
        model storage"""
        models.storage.delete(self)
