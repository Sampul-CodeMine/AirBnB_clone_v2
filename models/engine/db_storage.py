#!/usr/bin/python3
"""Importing some Standard modules and modules from our packages"""
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import MySQLdb

"""
This is a Python class that will be responsible for DB storage. In this
class, objects will be saved to a chosen DBMS (using MySQL for instance)
using SQLAlchemy ORM
"""

project_classes = {"State", "City", "Amenity", "User", "Place", "Review"}


class DBStorage:
    """Database Storage Class

    Attributes:
    __engine: The SQLAlchemy ORM engine
    __session: The SQLAlchemy ORM session
    """
    __engine = None
    __session = None

    def __init__(self):
        """This public method initializes the connection to the DB and creates
        creates the table"""
        db_conn = MySQLdb.conn(host=getenv('HBNB_MYSQL_HOST'),
                               port=3306,
                               user=getenv('HBNB_MYSQL_USER'),
                               password=getenv('HBNB_MYSQL_PWD'),
                               database=getenv('HBNB_MYSQL_DB'))
        self.__engine = create_engine('mysql+mysqldb://',
                                      creator=lambda: db_conn,
                                      pool_pre_ping=True)
        self.reload()

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def new(self, obj):
        """This is a public method that adds an object to the current database
        session
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """This is a public method that commits changes to the DB session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """This is a public method that removes an obj from the current DB
        session"""
        if obj is not None:
            self.__session.delet(obj)

    def close(self):
        """This is a public method that closes the current DB session
        """
        self.__session.close()

    def reload(self):
        """Public class method that creates DB and start a new DB session"""
        Base.metadata.create_all(self.__engine)
        safe_session = sessionmaker(bind=self.__enfine,
                                    expire_on_commit=False)
        Session = scoped_session(safe_session)
        self.__session = Session()

    def build_data(self, cls, data: dict):
        """public helper method to get rows and columns from the DB"""
        if type(data) == dict:
            sql = self.__session.query(cls)
            for row in sql.all():
                key = "{}.{}".format(cls.__name__, row.id)
                data[key] = row
            return (data)

    def all(self, cls=None):
        """Public method that returns data from the current DB session"""
        data = dict()
        if cls:
            return self.build_data(cls, data)
        for item in project_classes:
            data = self.build_data(eval(item), data)
        return (data)
