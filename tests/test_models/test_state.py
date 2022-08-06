#!/usr/bin/python3
"""Unittest test module
Test module for State class
"""
import unittest
import os
import pep8
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test case for the State class"""
    @classmethod
    def setUpClass(cls):
        """Setup test methods"""
        cls.state = State()
        cls.state.name = "LA"

    @classmethod
    def teardown(cls):
        """Tear down state function"""
        del cls.state

    def tearDown(self):
        """Tear down function"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_stat(self):
        """Test/checks for pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/state.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstring_stat(self):
        """Test/checks for docstring"""
        self.assertIsNotNone(State.__doc__)

    def test_attr_stat(self):
        """Test/checks for attributes"""
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.assertTrue('name' in self.state.__dict__)

    def test_inheritance_stat(self):
        """Test/checks for inheritance"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_attrtype_stat(self):
        """Test/checks for attribute type"""
        self.assertEqual(type(self.state.name), str)

    def test_save(self):
        """Test/checks for save function"""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict(self):
        """Test/checks for dictionary function"""
        self.assertEqual('to_dict' in dir(self.state), True)


if __name__ == "__main__":
    unittest.main()
