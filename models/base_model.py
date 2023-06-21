#!/usr/bin/python3
"""Importing some Standard modules and modules from our packages"""
import uuid as uid
import models
from datetime import datetime as dt
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey


"""
This is a Python class that will be the Base class or Parent class from which
all other classes will inherit from.
"""

Base = declarative_base()


class BaseModel():
    """
    This is a class modelling the BaseModel object for AirBnB Clone project.
    """
    """ creating class properties """
    id = Column("id", String(60), primary_key=True, nullable=False)
    created_at = Column("created_at", DateTime, nullable=False,
                        default=dt.utcnow())
    updated_at = Column("updated_at", DateTime, nullable=False,
                        default=dt.utcnow())

    def __init__(self, *args, **kwargs) -> None:
        """This is the constructor for the BaseModel class that instantiates
        an instance of the BaseModel object when created.

        Args:
            args (any) - non-keyworded arguments
            kwargs (any) - keyworded key and valued paired arguments
        """
        if kwargs != {} and kwargs is not None and bool(kwargs):
            # for key in kwargs:
            #     if key in ["created_at", "updated_at"]:
            #         self.__dict__[key] = dt.fromisoformat(kwargs[key])
            #     else:
            #         self.__dict__[key] = kwargs[key]
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = dt.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
                if 'id' not in kwargs:
                    self.id = str(uid.uuid4())
                if 'created_at' not in kwargs:
                    self.created_at = dt.now()

                if 'created_at' in kwargs and 'updated_at' not in kwargs:
                    self.updated_at = self.created_at
                else:
                    self.updated_at = dt.now()
        else:
            self.id = str(uid.uuid4())
            self.created_at = self.updated_at = dt.utcnow()

    def __str__(self) -> str:
        """Public instance method for the BaseModel that returns a String
        Representation of our BaseModel class"""
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def __repr__(self):
        """return a string representaion"""
        return self.__str__()

    def save(self) -> None:
        """Public instance method that updates the `updated_at` public
        instance property"""
        self.updated_at = dt.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self) -> dict:
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
