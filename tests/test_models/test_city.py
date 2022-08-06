#!/usr/bin/python3
"""Unittest test module
Test module for the class City
"""
import unittest
import pep8
import os
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Unittest test case for the City class"""
    @classmethod
    def setUp(cls):
        """Set up test model"""
        cls.testCity = City()
        cls.testCity.name = "lag"
        cls.testCity.state_id = "LA"

    @classmethod
    def tearDown(cls):
        """Delete test case"""
        del cls.testCity
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8_city(self):
        """Test/Checks for pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstrings_city(self):
        """Test/checks for docstrings"""
        self.assertTrue(len(City.__doc__) > 0)
        for func in dir(City):
            self.assertTrue(len(func.__doc__) > 0)

    def test_init_and_class_variables_city(self):
        """Test/checks for init and class variables"""
        self.assertTrue(isinstance(self.testCity, City))
        self.assertTrue(issubclass(type(self.testCity), BaseModel))
        self.assertTrue(self.testCity.name == "lag")
        self.assertTrue(self.testCity.state_id == "LA")
        self.assertIsNotNone(self.testCity.id)
        self.assertIsNotNone(self.testCity.updated_at)
        self.assertIsNotNone(self.testCity.created_at)

    def test_save_city(self):
        """Test/checks for save"""
        self.testCity.save()
        self.assertTrue(self.testCity.updated_at != self.testCity.created_at)


if __name__ == "__main__":
    unittest.main()
