#!/usr/bin/python3
"""Module for Base class
Contains attributes/methods for other classes
Base class for AirBnB clone console
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Base model class for project"""
    def __init__(self, *args, **kwargs):
        """Initializes a Base class"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """Return string representation of the Base model"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
        """Returns string function representation"""
        return self.__str__()

    def save(self):
        """Updates the save function with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns dictionary representation"""
        copy = dict(self.__dict__)
        copy['__class__'] = str(self.__class__.__name__)
        copy['created_at'] = self.created_at.isoformat()
        copy['updated_at'] = self.updated_at.isoformat()
        return copy
