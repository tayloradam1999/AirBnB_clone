#!/usr/bin/python3
"""
    Module for FileStorage class
    JSON -> file serialization and file -> JSON deserialization
"""

import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage:

    """ Manages read/write and serialization for JSON file store """
    __file_path = "file.json"
    __objects = dict()  # keyed with <class name>.id
    __models = dict({("BaseModel", BaseModel), ("User", User)})

    def all(self):
        """ Returns dict of __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Add a new object to __objects """
        k = "{}.{}".format(type(obj).__name__, obj.id)
        if k not in FileStorage.__objects.keys():
            FileStorage.__objects[k] = obj

    def remove(self, key):
        """Removes instance and saves to json file"""
        del FileStorage.__objects[key]
        FileStorage.save(self)

    def update(self, obj, key, value):
        """Updates an instance and saves to json file"""
        setattr(obj, key, value)
        FileStorage.save(self)

    def save(self):
        """ Serialize objects to JSON file in __file_path """
        d = dict()
        for k in FileStorage.__objects.keys():
            d[k] = FileStorage.__objects[k].to_dict()
        with open(FileStorage.__file_path, 'w') as fp:
            json.dump(d, fp)

    def reload(self):
        """ Deserializes the JSON file to __objects (if file exists) """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as fp:
                objs = json.load(fp)
                for k in objs.keys():
                    # insert to __objects if not exists
                    if k not in FileStorage.__objects.keys():
                        obj_data = objs[k]
                        cls = FileStorage.__models[obj_data["__class__"]]
                        FileStorage.__objects[k] = cls(**obj_data)
