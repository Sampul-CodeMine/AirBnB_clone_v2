#!/usr/bin/python3
"""Importing some Standard modules and modules from our packages"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import Session
from os import getenv
project_classes = {"State": State, "City": City, "Amenity": Amenity,
                   "User": User, "Place": Place, "Review": Review}

"""
This is a Python class that will be responsible for DB storage. In this
class, objects will be saved to a chosen DBMS (using MySQL for instance)
using SQLAlchemy ORM
"""


class DBStorage:
    """Database Storage Class

    Attributes:
    __engine: The SQLAlchemy ORM engine
    __session: The SQLAlchemy ORM session
    """
    __engine = None
    __session = None

    def __init__(self) -> None:
        """This public method initializes the connection to the DB and creates
        creates the table"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        """drop tables if test environment"""
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def new(self, obj) -> None:
        """This is a public method that adds an object to the current database
        session
        """
        if obj:
            self.__session.add(obj)

    def save(self) -> None:
        """This is a public method that commits changes to the DB session
        """
        self.__session.commit()

    def delete(self, obj=None) -> None:
        """This is a public method that removes an obj from the current DB
        session"""
        if obj:
            cls = project_classes[typ(obj).__name__]
            self.__session.query(cls).filter(cls.id == obj.id).delete()

    def close(self) -> None:
        """This is a public method that closes the current DB scoped session
        """
        self.__session.remove()

    def reload(self) -> None:
        """Public class method that creates DB and start a new DB session"""
        Base.metadata.create_all(self.__engine)
        safe_session = sessionmaker(bind=self.__engine,
                                    expire_on_commit=False)
        self.__session = scoped_session(safe_session)

    def all(self, cls=None) -> dict:
        """Public method that returns data from the current DB session"""
        data = dict()
        if cls:
            for field in self.__session.query(cls).all():
                data.update({"{}.{}".format(type(cls).__name__,
                                            field.id,): field})
        else:
            for k, v in project_classes.items():
                for field in self.__session.query(v):
                    data.update({"{}.{}".format(type(field).__name__,
                                                field.id,): field})
        return (data)
