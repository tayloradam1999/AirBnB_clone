"""
    Module for models dict
"""

from models.base_model import BaseModel
from models.user import User

model_classes = dict({("BaseModel", BaseModel), ("User", User)})
