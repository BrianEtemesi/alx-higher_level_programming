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

    def test_rec(self):
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 20)
        self.assertEqual(self.r2.x, 3)
        self.assertEqual(self.r2.y, 5)
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 4)



if __name__ == '__main__':
    unittest.main()
