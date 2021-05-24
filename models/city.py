#!/usr/bin/python3
"""
    Module for Cities model
"""
from models.base_model import BaseModel


class City(BaseModel):

    """
        Info on AirBnB Cities
        Public class attributes:
            state_id: string - empty string: it will be the State.id
            name: string - empty string
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_dict(self):
        return super(City, self).to_dict()
