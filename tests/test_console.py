#!/usr/bin/python3
"""Unittest tests
Test for the console command interpreter
"""
import unittest
from io import StringIO
from unittest.mock import patch
import pep8
import os
import console
import tests
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Unittest for command interpreter"""
    @classmethod
    def setUpClass(cls):
        """Setup test for console class"""
        cls.consol = HBNBCommand()

    @classmethod
    def teardown(cls):
        """Teardown test for console class"""
        del cls.consol

    def tearDown(self):
        """Delete temporary file created"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_console(self):
        """Test Pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["console.py"])
        self.assertEqual(p.total_errors, 0, 'fix Pep8')

    def test_docstrings_in_console(self):
        """Check/test for docstrings"""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)

    def test_emptyline(self):
        """Test for emtyline/no user input"""
        with patch('sys.stdout', new=StringIO()) as files:
            self.consol.onecmd("test")
            self.assertEqual("*** Unknown syntax: test\n", files.getvalue())

    def test_quit(self):
        """Test the quit command"""
        with patch('sys.stdout', new=StringIO()) as files:
            self.consol.onecmd("quit")
            self.assertEqual('', files.getvalue())
