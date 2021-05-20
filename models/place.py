#!/usr/bin/python3
"""
    Module for Place model
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
        Info on AirBnB Places
        Public class attributes:
            city_id: string - empty string: it will be the City.id
            user_id: string - empty string: it will be the User.id
            name: string - empty string
            description: string - empty string
            number_rooms: integer - 0
            number_bathrooms: integer - 0
            max_guest: integer - 0
            price_by_night: integer - 0
            latitude: float - 0.0
            longitude: float - 0.0
            amenity_ids: list of string - empty list: it will be the
                list of Amenity.id later
    """
    pass
