#!/usr/bin/python3
"""
    Module for User model
"""
from models.base_model import BaseModel


class User(BaseModel):

    """
        Info on AirBnB Users
        Public class attributes:
            email: string - empty string
            password: string - empty string
            first_name: string - empty string
            last_name: string - empty string
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_dict(self):
        return super(User, self).to_dict()

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = str(value)

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = str(value)

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = str(value)

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = str(value)
