#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

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
    classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review}

    def all(self, cls=None) -> dict:
        """
        This is a public instance method that returns the private instance
        attribute `__object` which is a dictionary

        Return:
            A dictionary of objects
        """
        objs = {}
        if cls is not None:
            if cls.__name__ in FileStorage.classes:
                for k, v in self.__objects.items():
                    if k.split('.')[0] == cls.__name__:
                        objs.update({k: v})
        else:
            objs = self.__objects
        return (objs)

    def new(self, obj) -> None:
        """
        This is a public instance method that adds a new object to the
        dictionary of objects (`__objects`)

        Args:
            obj (dict) - a dictionaary object
        """
        if obj:
            item = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[item] = obj

    def save(self) -> None:
        """
        This is a public instance method that serializes the private instance
        attribute `__objects` (dict) into a JSON string and save it to a flat
        database (json file)
        """
        with open(FileStorage.__file_path, 'w', encoding='UTF-8') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self) -> None:
        """
        This is a public instance method that deserializes a json string into
        a dictionary of object, `__objects` only if `__file_path` exist.
        """
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = \
                        FileStorage.classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None) -> None:
        """This is a public instance method that deletes an object from the
        class private __object property.

        Args:
            obj (dict): the object to delete from __object
        """
        if obj:
            item = "{}.{}".format(type(obj).__name__, obj.id)
            if self.__objects[item]:
                del self.__objects[item]
                self.save()

    def close(self) -> None:
        """This is a class public instance method that Deserialize JSON file
        to objects and then call the reload method."""
        self.reload()
