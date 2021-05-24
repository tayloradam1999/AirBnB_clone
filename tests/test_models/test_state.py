#!/usr/bin/python3
"""
    Unit test module for State class
"""
import unittest
import os
from models.engine.file_storage import FileStorage
from datetime import datetime
from models.state import State


state1 = State()


class TestState(unittest.TestCase):

    """ Class for State tests """

    def test_id(self):
        """ Unittesting test_id instance """
        self.assertTrue(isinstance(state1.id, str))

    def test_name(self):
        """ Make sure name is string """
        self.assertTrue(isinstance(State.name, str))
        self.assertTrue(isinstance(state1.name, str))
