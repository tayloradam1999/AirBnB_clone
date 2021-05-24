#!/usr/bin/python3
"""
    Module for Review model
"""
from models.base_model import BaseModel


class Review(BaseModel):

    """
        Info on AirBnB Reviews
        Public class attributes:
            place_id: string - empty string: it will be the Place.id
            user_id: string - empty string: it will be the User.id
            text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_dict(self):
        return super(Review, self).to_dict()
