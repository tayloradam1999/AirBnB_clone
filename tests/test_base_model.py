#!/usr/bin/python3
"""
    Unit test module for BaseModel class
"""
import unittest
from models.base_model import BaseModel


class TestBaseModelMethods(unittest.TestCase):

    """ Class for BaseModel tests """

    def test_task_3(self):
        b1 = BaseModel()
        b1.name = "Holberton"
        self.assertEqual(b1.name, "Holberton")
        b1.my_number = 89
        self.assertEqual(b1.my_number, 89)
        print(b1)
        b1_json = b1.to_dict()
        print(b1_json)
        print("JSON of b1:")
        for k in b1_json.keys():
            print("\t{}: ({}) - {}".format(k, type(b1_json[k]), b1_json[k]))

if __name__ == '__main__':
    unittest.main()
