#!/usr/bin/python3
"""Module
FileStorage Class
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Class for serialization and deserialization of base classes"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns object dictionary"""
        return self.__objects

    def new(self, obj):
        """Set new obj in __objects dictionary"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serialize __objects to JSON file"""
        jsonData = {}
        for key, value in self.__objects.items():
            jsonData[key] = value.to_dict()
        with open(self.__file_path, 'w') as files:
            json.dump(jsonData, files)

    def reload(self):
        """Deserialize JSON file into __objects"""
        try:
            with open(self.__file_path, 'r') as files:
                data = json.load(files)
                for key, obj in data.items():
                    newObj = eval(obj['__class__'])(**obj)
                    self.__objects[key] = newObj
        except FileNotFoundError:
            pass
