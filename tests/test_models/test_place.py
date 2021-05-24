#!/usr/bin/python3
"""
    Unit test module for Place class
"""
import unittest
import os
from models.engine.file_storage import FileStorage
from datetime import datetime
from models.place import Place


place1 = Place()


class TestPlace(unittest.TestCase):

    """ Class for Place tests """

    def test_id(self):
        """ Unittesting test_id instance """
        self.assertTrue(isinstance(place1.id, str))

    def test_city_id(self):
        """ Make sure city_id is string """
        self.assertTrue(isinstance(Place.city_id, str))
        self.assertTrue(isinstance(place1.city_id, str))

    def test_user_id(self):
        """ Make sure user_id is string """
        self.assertTrue(isinstance(Place.user_id, str))
        self.assertTrue(isinstance(place1.user_id, str))

    def test_name(self):
        """ Make sure name is a string """
        self.assertTrue(isinstance(Place.name, str))
        self.assertTrue(isinstance(place1.name, str))

    def test_description(self):
        """ Make sure description is a string """
        self.assertTrue(isinstance(Place.description, str))
        self.assertTrue(isinstance(place1.description, str))

    def test_number_rooms(self):
        """ Make sure number of rooms is an int """
        self.assertTrue(isinstance(Place.number_rooms, int))
        self.assertTrue(isinstance(place1.number_rooms, int))

    def test_number_bathrooms(self):
        """ Make sure number_bathrooms is an int """
        self.assertTrue(isinstance(Place.number_bathrooms, int))
        self.assertTrue(isinstance(place1.number_bathrooms, int))

    def test_max_guest(self):
        """ Make sure max_guest is an int """
        self.assertTrue(isinstance(Place.max_guest, int))
        self.assertTrue(isinstance(place1.max_guest, int))

    def test_price_by_night(self):
        """ Make sure price_by_night is a integer """
        self.assertTrue(isinstance(Place.price_by_night, int))
        self.assertTrue(isinstance(place1.price_by_night, int))

    def test_latitude(self):
        """ Make sure latitude is a float """
        self.assertTrue(isinstance(Place.latitude, float))
        self.assertTrue(isinstance(place1.latitude, float))

    def test_longitude(self):
        """ Make sure longitude is a float """
        self.assertTrue(isinstance(Place.longitude, float))
        self.assertTrue(isinstance(place1.longitude, float))

    def test_amenity_ids(self):
        """ Make sure amenity_ids is a list """
        self.assertTrue(isinstance(Place.amenity_ids, list))
        self.assertTrue(isinstance(place1.amenity_ids, list))
