#!/usr/bin/python3
"""
This module contains unit tests for the rectangle
module
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.r1 = Rectangle(10, 20)
        self.r2 = Rectangle(5, 15, 3, 5, 4)
        self.r3 = Rectangle(8, 21,)

    def test_id(self):
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 4)
        self.assertEqual(self.r3.id, 2)


if __name__ == '__main__':
    unittest.main()
