#!/usr/bin/python3
"""
    Module for Amenity model
"""
from models.base_model import BaseModel


class Amenity(BaseModel):

    """
        Info on AirBnB Amenities
        Public class attributes:
            name: string - empty string
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_dict(self):
        return super(Amenity, self).to_dict()
