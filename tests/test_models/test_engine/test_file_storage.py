#!/usr/bin/python3
"""Unittest tests
Test for FileStorage class
"""
import unittest
import pep8
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test case for FileStorage class"""
    @classmethod
    def setUpClass(cls):
        """Setup tests methods"""
        cls.usr = User()
        cls.usr.first_name = "Chinomso"
        cls.usr.last_name = "Okoye"
        cls.usr.email = "chinomsokoye@gmail.com"
        cls.storage = FileStorage()

    @classmethod
    def teardown(cls):
        """Set up teardown"""
        del cls.usr

    def teardown(self):
        """Set up tear down"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_filestorage(self):
        """Test for Pep8 file storage"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_all_filestorage(self):
        """Test for all filestorage"""
        new = FileStorage()
        instances_dic = new.all()
        self.assertIsNotNone(instances_dic)
        self.assertEqual(type(instances_dic), dict)
        self.assertIs(instances_dic, new._FileStorage__objects)

    def test_new_filestorage(self):
        """Test for new filestorage"""
        altsotrage = FileStorage()
        dic = altsotrage.all()
        rev = User()
        rev.id = 69
        rev.name = "Emma"
        altsotrage.new(rev)
        key = rev.__class__.__name__ + "." + str(rev.id)
        self.assertIsNotNone(dic[key])

    def test_reload_filestorage(self):
        """Test for reload filestorage"""
        self.storage.save()
        Root = os.path.dirname(os.path.abspath("console.py"))
        path = os.path.join(Root, "file.json")
        with open(path, 'r') as files:
            lines = files.readlines()

        try:
            os.remove(path)
        except Exception:
            pass

        self.storage.save()

        with open(path, 'r') as files:
            lines2 = files.readlines()

        self.assertEqual(lines, lines2)

        try:
            os.remove(path)
        except Exception:
            pass

        with open(path, 'w') as files:
            files.write("{}")
        with open(path, 'r') as f:
            for line in f:
                self.assertEqual(line, "{}")
        self.assertIs(self.storage.reload(), None)


if __name__ == "__main__":
    unittest.main()
