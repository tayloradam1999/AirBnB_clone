#!/usr/bin/python3
""" Module for BaseModel class """
import uuid
from datetime import datetime


class BaseModel:

    """ BaseModel class """

    def __init__(self, *args, **kwargs):
        self.__id = str(uuid.uuid4())
        self.__created_at = datetime.now()
        self.__updated_at = datetime.now()
        if kwargs is not None:
            if "__class__" in kwargs.keys():
                del kwargs["__class__"]
            if "__created_at" in kwargs.keys():
                del kwargs["__created_at"]
            if "id" in kwargs.keys():
                self.__id = kwargs["id"]
                del kwargs["id"]
            for k in kwargs:
                if BaseModel.checkDate(kwargs[k]):
                    kwargs[k] = datetime.strptime(
                        kwargs[k],
                        "%Y-%m-%dT%H:%M:%S.%f")
            self.__dict__.update(kwargs)

    @staticmethod
    def checkDate(string):
        """ Checks if string is a date """
        try:
            datetime.strptime(string, "%Y-%m-%dT%H:%M:%S.%f")
            return True
        except ValueError:
            return False

    @staticmethod
    def formatDate(date):
        return str(date.strftime("%Y-%m-%dT%H:%M:%S.%f"))

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def created_at(self):
        return self.__created_at

    @property
    def updated_at(self):
        return self.__updated_at

    @updated_at.setter
    def updated_at(self, value):
        self.__updated_at = value

    def save(self):
        self.__updated_at = datetime.now()

    def to_dict(self):
        d = dict(self.__dict__)
        t = "_{}__".format(type(self).__name__)
        d = dict(
            map(lambda k: (k.replace(t, ""),
                str(d[k])), d))
        d["__class__"] = type(self).__name__
        return d

    def __str__(self):
        t = "[{}] ({}) {}"
        return t.format(type(self).__name__, self.id, self.to_dict())
