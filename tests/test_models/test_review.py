#!/usr/bin/python3
"""
    Unit test module for Review class
"""
import unittest
import os
from models.engine.file_storage import FileStorage
from datetime import datetime
from models.review import Review


review1 = Review()


class TestReview(unittest.TestCase):

    """ Class for Review tests """

    def test_id(self):
        """ Unittesting test_id instance """
        self.assertTrue(isinstance(review1.id, str))

    def test_place_id(self):
        """ Make sure place_id is string """
        self.assertTrue(isinstance(Review.place_id, str))
        self.assertTrue(isinstance(review1.place_id, str))

    def test_user_id(self):
        """ Make sure user_id is string """
        self.assertTrue(isinstance(Review.user_id, str))
        self.assertTrue(isinstance(review1.user_id, str))

    def test_text(self):
        """ Make sure text is string """
        self.assertTrue(isinstance(Review.text, str))
        self.assertTrue(isinstance(review1.text, str))
