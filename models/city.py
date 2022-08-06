#!/usr/bin/python3
"""Module for city class
Inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class inherits from BaseModel"""
    state_id = ""
    name = ""
