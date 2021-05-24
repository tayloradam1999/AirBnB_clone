#!/usr/bin/python3
"""
    Unit test module for User class
"""
import unittest
import os
from models.engine.file_storage import FileStorage
from datetime import datetime
from models.user import User


user1 = User()


class TestUser(unittest.TestCase):

    """ Class for User tests """

    def test_id(self):
        """ Unittesting test_id instance """
        self.assertTrue(isinstance(user1.id, str))

    def test_email(self):
        """ Make sure email is string """
        self.assertTrue(isinstance(User.email, str))
        self.assertTrue(isinstance(user1.email, str))
