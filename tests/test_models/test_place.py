#!/usr/bin/python3
"""Unittest test module
Test modul for class Place
"""
import unittest
import os
import pep8
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test case for Place class"""
    @classmethod
    def setUpClass(cls):
        """Set up the model class"""
        cls.testPlace = Place()
        cls.testPlace.city_id = "somewhere"
        cls.testPlace.user_id = "test"
        cls.testPlace.name = "test1"
        cls.testPlace.description = "test it"
        cls.testPlace.number_rooms = 0
        cls.testPlace.number_bathrooms = 0
        cls.testPlace.max_guest = 0
        cls.testPlace.price_by_night = 0
        cls.testPlace.latitude = 0.0
        cls.testPlace.longitude = 0.0
        cls.testPlace.amenity_ids = []

    @classmethod
    def tearDownClass(cls):
        """Delete test Place created"""
        del cls.testPlace
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8(self):
        """Test/checks for pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/place.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstrings(self):
        """Test/checks for docstrings"""
        self.assertTrue(len(Place.__doc__) > 0)
        for func in dir(Place):
            self.assertTrue(len(func.__doc__) > 0)

    def test_subclass(self):
        """Tests/checks for subclass"""
        self.assertTrue(issubclass(self.testPlace.__class__, BaseModel), True)

    def test_attributes_and_init(self):
        """Test/checks for attributes and init"""
        self.assertTrue(isinstance(self.testPlace, Place))
        self.assertTrue('id' in self.testPlace.__dict__)
        self.assertTrue('created_at' in self.testPlace.__dict__)
        self.assertTrue('updated_at' in self.testPlace.__dict__)
        self.assertTrue('city_id' in self.testPlace.__dict__)
        self.assertTrue('user_id' in self.testPlace.__dict__)
        self.assertTrue('name' in self.testPlace.__dict__)
        self.assertTrue('description' in self.testPlace.__dict__)
        self.assertTrue('number_rooms' in self.testPlace.__dict__)
        self.assertTrue('number_bathrooms' in self.testPlace.__dict__)
        self.assertTrue('max_guest' in self.testPlace.__dict__)
        self.assertTrue('price_by_night' in self.testPlace.__dict__)
        self.assertTrue('latitude' in self.testPlace.__dict__)
        self.assertTrue('longitude' in self.testPlace.__dict__)
        self.assertTrue('amenity_ids' in self.testPlace.__dict__)

    def test_has_strings(self):
        """Test/checks for has_strings"""
        self.assertEqual(type(self.testPlace.city_id), str)
        self.assertEqual(type(self.testPlace.user_id), str)
        self.assertEqual(type(self.testPlace.name), str)
        self.assertEqual(type(self.testPlace.description), str)
        self.assertEqual(type(self.testPlace.number_rooms), int)
        self.assertEqual(type(self.testPlace.number_bathrooms), int)
        self.assertEqual(type(self.testPlace.max_guest), int)
        self.assertEqual(type(self.testPlace.price_by_night), int)
        self.assertEqual(type(self.testPlace.latitude), float)
        self.assertEqual(type(self.testPlace.longitude), float)
        self.assertEqual(type(self.testPlace.amenity_ids), list)

    def test_save(self):
        """Test/checks for save"""
        self.testPlace.save()
        self.assertNotEqual(self.testPlace.created_at,
                            self.testPlace.updated_at)

    def test_to_dict(self):
        """Test/checks for to_dict"""
        self.assertEqual('to_dict' in dir(self.testPlace), True)


if __name__ == "__main__":
    unittest.main()
