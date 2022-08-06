#!/usr/bin/python3
"""Unittest test module
Test module for BaseModel class
"""
import unittest
import os
import pep8
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittest case for BaseModel class"""
    @classmethod
    def setUpClass(cls):
        """Set up class method"""
        cls.testBase = BaseModel()
        cls.testBase.x = "x"
        cls.testBase.y = 100

    @classmethod
    def tearDownClass(cls):
        """Tear down class method"""
        del cls.testBase
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_basemodel(self):
        """Test for pep8 basemodel"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_check_functions(self):
        """Test/check for functions"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_attribute_basemodel(self):
        """Test/check for basemodel attribute"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init(self):
        """Test/check for init"""
        self.assertTrue(isinstance(self.testBase, BaseModel))

    def test_save(self):
        """Test/check for save"""
        self.testBase.save()
        self.assertNotEqual(self.testBase.created_at, self.testBase.updated_at)

    def test_to_dict(self):
        """Test/check for to_dict"""
        copy = self.testBase.to_dict()
        self.assertEqual(self.testBase.__class__.__name__, 'BaseModel')
        self.assertIsInstance(copy['created_at'], str)
        self.assertIsInstance(copy['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
