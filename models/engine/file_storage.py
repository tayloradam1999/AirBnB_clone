#!/usr/bin/python3
""" 
    Module for FileStorage class
    JSON -> file serialization and file -> JSON deserialization
"""

import json
import os
from models.base_model import BaseModel


class FileStorage:
    """ Manages read/write and serialization for JSON file store """
    __file_path ="HBNB_jsonfile.json"
    __objects = dict() #keyed with <class name>.id

    def all(self):
        """ Returns dict of __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Add a new object to __objects """
        k = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[k] = obj.to_dict()

    def save(self):
        """ Serialize objects to JSON file in __file_path """
        with open(FileStorage.__file_path, 'w') as fp:
            json.dump(FileStorage.__objects, fp)

    def reload(self):
        """ Deserializes the JSON file to __objects (if file exists) """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as fp:
                FileStorage.__objects = json.load(fp)

