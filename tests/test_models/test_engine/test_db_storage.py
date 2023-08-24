#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.state import State
from models import storage
import os

class test_dbStorage(unittest.TestCase):
    """ Class to test the database storage """

    def test_storage_count(self):
        """ Tests the count method of FileStorage """
        count = storage.count()
        new = State()
        new.name = "NEW_STATE1"
        new.save()
        new_count = storage.count()
        self.assertTrue(new_count > count)

    def test_storage_get(self):
        """ Tests the get method of FileStorage """
        new = State()
        new.name = "NEW_STATE2"
        new.save()
        self.assertEqual(new, storage.get(State, new.id))
