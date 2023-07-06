#!/usr/bin/python3
"""Importing some Standard modules and modules from our packages"""
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

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
        self.__session.add(obj)

    def save(self) -> None:
        """This is a public method that commits changes to the DB session
        """
        self.__session.commit()

    def delete(self, obj=None) -> None:
        """This is a public method that removes an obj from the current DB
        session"""
        if obj is not None:
            self.__session.delete(obj)

    def close(self) -> None:
        """This is a public method that closes the current DB scoped session
        """
        self.__session.close()

    def reload(self) -> None:
        """Public class method that creates DB and start a new DB session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def all(self, cls=None) -> dict:
        """Public method that returns data from the current DB session"""
        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}
