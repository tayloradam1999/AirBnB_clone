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
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_dict(self):
        return super(User, self).to_dict()
