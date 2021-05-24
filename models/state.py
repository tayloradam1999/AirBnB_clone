#!/usr/bin/python3
"""
    Module for State model
"""
from models.base_model import BaseModel


class State(BaseModel):

    """
        Info on AirBnB States
        Public class attributes:
            name: string - empty string
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_dict(self):
        return super(State, self).to_dict()
