#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

"""
This is a Python class that will be responsible for file storage. In this
class, objects will be serialized into a JSON string object and saved to a
flat database (json file)
"""


class FileStorage:
    """
    This is a class responsible for data storage for AirBnB Clone project.
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None) -> dict:
        """
        This is a public instance method that returns the private instance
        attribute `__object` which is a dictionary

        Return:
            A dictionary of objects
        """
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            cls_dict = {}
            for k, v in self.__objects.items():
                if type(v) == cls:
                    cls_dict[k] = v
            return cls_dict
        return self.__objects

    def new(self, obj) -> None:
        """
        This is a public instance method that adds a new object to the
        dictionary of objects (`__objects`)

        Args:
            obj (dict) - a dictionaary object
        """
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self) -> None:
        """
        This is a public instance method that serializes the private instance
        attribute `__objects` (dict) into a JSON string and save it to a flat
        database (json file)
        """
        odict = {o: self.__objects[o].to_dict() for o in self.__objects.keys()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(odict, f)

    def reload(self) -> None:
        """
        This is a public instance method that deserializes a json string into
        a dictionary of object, `__objects` only if `__file_path` exist.
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                for o in json.load(f).values():
                    name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(name)(**o))
        except FileNotFoundError:
            pass

    def delete(self, obj=None) -> None:
        """This is a public instance method that deletes an object from the
        class private __object property.

        Args:
            obj (dict): the object to delete from __object
        """
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (AttributeError, KeyError):
            pass

    def close(self) -> None:
        """This is a class public instance method that Deserialize JSON file
        to objects and then call the reload method."""
        self.reload()
