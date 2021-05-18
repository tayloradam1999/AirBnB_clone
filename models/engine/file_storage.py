#!/usr/bin/python3
""" 
    Module for FileStorage class
    JSON -> file serialization and file -> JSON deserialization
"""


class FileStorage:
    """ Manages read/write and serialization for JSON file store """
    __file_path = "<path to the JSON file>"
    __objects = dict() #keyed with <class name>.id

    def all(self):
        """ Returns dict of __objects """
        return self.__objects

    def new(self, obj):
        """ Add a new object to __objects """
        pass

    def save(self):
        """ Serialize objects to JSON file in __file_path """
        pass

    def reload(self):
        """ Deserializes the JSON file to __objects (if file exists) """
        pass

