#!/usr/bin/python3
"""
    Unit test module for City class
"""
import unittest
import os
from models.engine.file_storage import FileStorage
from datetime import datetime
from models.city import City


city1 = City()


class TestCity(unittest.TestCase):

    """ Class for City tests """

    def test_id(self):
        """ Unittesting test_id instance """
        self.assertTrue(isinstance(city1.id, str))

    def test_state_id(self):
        """ Make sure state_id is string """
        self.assertTrue(isinstance(City.state_id, str))
        self.assertTrue(isinstance(city1.state_id, str))

    def test_last_name(self):
        """ Make sure name is string """
        self.assertTrue(isinstance(City.name, str))
        self.assertTrue(isinstance(city1.name, str))
