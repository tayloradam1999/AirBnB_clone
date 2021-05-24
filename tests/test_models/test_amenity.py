#!/usr/bin/python3
"""
    Unit test module for Amenity class
"""
import unittest
import os
from models.engine.file_storage import FileStorage
from datetime import datetime
from models.amenity import Amenity


amenity1 = Amenity()


class TestAmenity(unittest.TestCase):

    """ Class for Amenity tests """

    def test_id(self):
        """ Unittesting test_id instance """
        self.assertTrue(isinstance(amenity1.id, str))

    def test_name(self):
        """ Make sure name is string """
        self.assertTrue(isinstance(Amenity.name, str))
        self.assertTrue(isinstance(amenity1.name, str))
