#!/usr/bin/python3
"""Importing some Standard modules and modules from our packages"""
from os import getenv
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
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
            self.__session.delete(obj)

    def close(self):
        """This is a public method that closes the current DB session
        """
        self.__session.close()

    def reload(self):
        """Public class method that creates DB and start a new DB session"""
        Base.metadata.create_all(self.__engine)
        safe_session = sessionmaker(bind=self.__engine,
                                    expire_on_commit=False)
        Session = scoped_session(safe_session)
        self.__session = Session()

    def all(self, cls=None):
        """Public method that returns data from the current DB session"""
        data = dict()
        if cls:
            if type(cls) == str:
                cls.eval(cls)
            obj = self.__session.query(cls)
        elif cls is None:
            obj = self.__session.query(Amenity).all()
            obj = self.__session.query(City).all()
            obj = self.__session.query(Place).all()
            obj = self.__session.query(Review).all()
            obj = self.__session.query(State).all()
            obj = self.__session.query(User).all()
        return ({"{}.{}".format(type(ob).__name__, ob.id): ob for ob in obj})
