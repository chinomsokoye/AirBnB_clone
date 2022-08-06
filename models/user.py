#!/usr/bin/python3
"""Module User class
Inherits from Base model
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class inheriting from Base model"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
