#!/usr/bin/python3
"""Unittest test
Test for Amenity class
"""
import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel
import pep8


class TestAmenity(unittest.TestCase):
    """Test case for the Amenity class"""
    @classmethod
    def setUpClass(cls):
        """Set up test for amenity"""
        cls.lord = Amenity()
        cls.lord.name = "Breakfast"

    @classmethod
    def teardown(cls):
        """Set up teardown test"""
        del cls.lord

    def tearDown(self):
        """Set up the tearDown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Amen(self):
        """Test for pep8 Amenity"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstring_Amen(self):
        """Test for docstring"""
        self.assertIsNotNone(self.lord.__doc__)

    def test_attr_Amen(self):
        """Test/checks for attributes in amenity"""
        self.assertTrue('id' in self.lord.__dict__)
        self.assertTrue('created_at' in self.lord.__dict__)
        self.assertTrue('updated_at' in self.lord.__dict__)
        self.assertTrue('name' in self.lord.__dict__)

    def test_inheritance_Amen(self):
        """Test for inheritance"""
        self.assertTrue(issubclass(self.lord.__class__, BaseModel), True)

    def test_attrtype_Amen(self):
        """Test for attribute types in inheritance"""
        self.assertEqual(type(self.lord.name), str)

    def test_save(self):
        """Test the save function ()"""
        self.lord.save()
        self.assertNotEqual(self.lord.created_at, self.lord.updated_at)

    def test_to_dict(self):
        """Test for dictionary function"""
        self.assertEqual('to_dict' in dir(self.lord), True)


if __name__ == "__main__":
    unittest.main()
