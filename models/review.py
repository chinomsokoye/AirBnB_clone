#!/usr/bin/python3
"""Module Review class
Inherits from Base Model
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class inheriting from Base model"""
    place_id = ""
    user_id = ""
    text = ""
