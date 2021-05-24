"""
    Module for models dict
"""

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity

model_classes = dict({
    ("BaseModel", BaseModel),
    ("User", User),
    ("State", State),
    ("City", City),
    ("Place", Place),
    ("Amenity", Amenity),
    ("Review", Review)})
