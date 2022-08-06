#!/usr/bin/python3
"""Unittest test
Test module for User class
"""
import unittest
import pep8
import os
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test case for the User class"""
    @classmethod
    def setUp(cls):
        """Set up class method"""
        cls.testUser = User()
        cls.testUser.email = "email"
        cls.testUser.password = "passwd"
        cls.testUser.first_name = "first_name"
        cls.testUser.last_name = "last_name"

    @classmethod
    def tearDown(cls):
        """Delete test class method"""
        del cls.testUser
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8(self):
        """Test/checks pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/user.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstrings(self):
        """Test/checks for docstrings"""
        self.assertTrue(len(User.__doc__) > 0)
        for func in dir(User):
            self.assertTrue(len(func.__doc__) > 0)

    def test_init_and_class_variables(self):
        """Test/checks for init and class variables"""
        self.assertTrue(isinstance(self.testUser, User))
        self.assertTrue(issubclass(type(self.testUser), BaseModel))
        self.assertTrue('email' in self.testUser.__dict__)
        self.assertTrue('id' in self.testUser.__dict__)
        self.assertTrue('created_at' in self.testUser.__dict__)
        self.assertTrue('updated_at' in self.testUser.__dict__)
        self.assertTrue('password' in self.testUser.__dict__)
        self.assertTrue('first_name' in self.testUser.__dict__)
        self.assertTrue('last_name' in self.testUser.__dict__)

    def test_save(self):
        """Test/checks for save function"""
        self.testUser.save()
        self.assertTrue(self.testUser.updated_at != self.testUser.created_at)

    def test_strings(self):
        """Test/checks for strings"""
        self.assertEqual(type(self.testUser.email), str)
        self.assertEqual(type(self.testUser.password), str)
        self.assertEqual(type(self.testUser.first_name), str)
        self.assertEqual(type(self.testUser.last_name), str)

    def test_to_dict(self):
        """Test/checks for to_dict function"""
        self.assertEqual('to_dict' in dir(self.testUser), True)


if __name__ == "__main__":
    unittest.main()
