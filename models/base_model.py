#!/usr/bin/python3
""" Module for BaseModel class """
import uuid
from datetime import datetime
import models


class BaseModel:

    """ BaseModel class """

    def __init__(self, *args, **kwargs):

        uid = str(uuid.uuid4())
        self.id = uid if "id" not in kwargs else kwargs["id"]
        n = datetime.now()
        self.created_at = n if "created_at" not in kwargs else kwargs[
            "created_at"]
        self.updated_at = n if "updated_at" not in kwargs else kwargs[
            "updated_at"]
        if kwargs is not None:
            if "__class__" in kwargs.keys():
                del kwargs["__class__"]
            if "id" in kwargs.keys():
                self.__id = kwargs["id"]
                del kwargs["id"]
            self.__dict__.update(kwargs)
        models.storage.new(self)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def created_at(self):
        return self.__created_at

    @created_at.setter
    def created_at(self, value):
        if isinstance(value, str):
            self.__created_at = datetime.strptime(
                value, "%Y-%m-%d %H:%M:%S.%f")
        else:
            self.__created_at = value

    @property
    def updated_at(self):
        return self.__updated_at

    @updated_at.setter
    def updated_at(self, value):
        if isinstance(value, str):
            self.__updated_at = datetime.strptime(
                value, "%Y-%m-%d %H:%M:%S.%f")
        else:
            self.__updated_at = value

    def save(self):
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        d = dict(self.__dict__)
        t = "_{}__".format(type(self).__name__)
        d = dict(
            map(lambda k: (k.replace(t, "").replace("_BaseModel__", ""),
                str(d[k])), d))
        d["__class__"] = type(self).__name__
        return d

    def __str__(self):
        t = "[{}] ({}) {}"
        return t.format(type(self).__name__, self.id, self.to_dict())
