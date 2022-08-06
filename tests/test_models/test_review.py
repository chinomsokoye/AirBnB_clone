#!/usr/bin/python3
"""Unittest test module
Test module for the Review class
"""
import unittest
import os
from models.review import Review
from models.base_model import BaseModel
import pep8


class TestReview(unittest.TestCase):
    """Test case for the Review class"""
    @classmethod
    def setUpClass(cls):
        """Set up class functions"""
        cls.newreview = Review()
        cls.newreview.place_id = "101010101"
        cls.newreview.user_id = "mel"
        cls.newreview.text = "Best school"

    @classmethod
    def teardown(cls):
        """Delete test methods"""
        del cls.newreview

    def tearDown(self):
        """Delete test methods"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_review(self):
        """Test/check for pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/review.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstring_review(self):
        """Test/checks for docstring"""
        self.assertIsNotNone(Review.__doc__)

    def test_attributes_review(self):
        """Test/checks for attributes"""
        self.assertTrue('id' in self.newreview.__dict__)
        self.assertTrue('created_at' in self.newreview.__dict__)
        self.assertTrue('updated_at' in self.newreview.__dict__)
        self.assertTrue('place_id' in self.newreview.__dict__)
        self.assertTrue('text' in self.newreview.__dict__)
        self.assertTrue('user_id' in self.newreview.__dict__)

    def test_subclass_review(self):
        """Test/checks for subclass"""
        self.assertTrue(issubclass(self.newreview.__class__, BaseModel), True)

    def test_attr_types_review(self):
        """Test/checks for attribute types"""
        self.assertEqual(type(self.newreview.text), str)
        self.assertEqual(type(self.newreview.place_id), str)
        self.assertEqual(type(self.newreview.user_id), str)

    def test_save(self):
        """Test/checks for save function"""
        self.newreview.save()
        self.assertNotEqual(self.newreview.created_at,
                            self.newreview.updated_at)

    def test_to_dict(self):
        """Test/checks for dictionary"""
        self.assertEqual('to_dict' in dir(self.newreview), True)


if __name__ == "__main__":
    unittest.main()
