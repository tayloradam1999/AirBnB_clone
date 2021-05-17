#!/usr/bin/python3
""" Module for BaseModel class """
import uuid
from datetime import datetime


class BaseModel:

    """ BaseModel class """

    def __init__(self):
        self.__id = str(uuid.uuid4())
        self.__created_at = datetime.now()
        self.__updated_at = datetime.now()

    @staticmethod
    def formatDate(date):
        return date.strftime("%Y-%m-%dT%H:%M:%S.%f")

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def created_at(self):
        return BaseClass.formatDate(self.__created_at)

    @property
    def updated_at(self):
        return BaseClass.formatDate(self.__updated_at)

    def save(self):
        self.__updated_at = datetime.now()

    def to_dict(self):
        d = dict(self.__dict__)
        t = "_{}__".format(type(self).__name__)
        d = dict(map(lambda k: (k.replace(t, ""), d[k]), d))
        d["__class__"] = type(self).__name__
        return d

    def __str__(self):
        t = "[{}] ({}) {}"
        return t.format(type(self).__name__, self.id, self.__dict__)
