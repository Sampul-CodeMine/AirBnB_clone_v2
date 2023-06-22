#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


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
        Attributes:
            cls (class): a class which is by default None
        Return:
            A dictionary of objects
        """
        if cls:
            of_same_type = dict()
            for key, val in self.__objects.items():
                if val.__class__ == cls:
                    of_same_type[key] = val
            return of_same_type

        return FileStorage.__objects

    def new(self, obj) -> None:
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self) -> None:
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self) -> None:
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None) -> None:
        """This is a public instance method that deletes an object from the
        class private __object property.

        Args:
            obj (dict): the object to delete from __object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)

            if self.__objects[key]:
                del self.__objects[key]
                self.save()
