#!/usr/bin/python3
""" Unittest module for the console """

import unittest
from unittest.mock import patch
from io import StringIO
import pep8
import os
import json
import console
import tests
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestCommand(unittest.TestCase):
    """ Class that test the console """

    def setUp(self):
        """ Function empties file.json """
        FileStorage._FileStorage__objects = {}
        FileStorage().save()

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "Not FileStorage")
    def test_create_fs(self):
        """ test the create command """
        pass

    def testPycodeStyle(self):
        """ Pycodestyle test for the console """
        style = pycodestyle.StyleGuide(quiet=True)
        p = style.check_files(['console.py'])
        self.assertEqual(p.total_error, 0, "fix pep8")

    def test_doc_console(self):
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)


if __name__ == '__main__':
    unittest.main()
