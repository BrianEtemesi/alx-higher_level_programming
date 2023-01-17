#!/usr/bin/python3
"""
This is a unit test module for the Base
class module
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """test the Base class"""

    def testBase(self):

        a = Base()
        b = Base()
        c = Base(7)

        self.assertEqual(a.id, 1)
        self.assertEqual(b.id, 2)
        self.assertEqual(c.id, 7)


