#!/usr/bin/python3
"""
This module contains unit tests for the rectangle
module
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):


    def setUp(self):
        Base._Base__nb_objects = 0
        self.r1 = Rectangle(10, 20)
        self.r2 = Rectangle(5, 15, 3, 5, 4)
        self.r3 = Rectangle(8, 21,)

    def test_id(self):
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 4)
        self.assertEqual(self.r3.id, 2)

    def test_width(self):

        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r2.width, 5)

        self.r1.width = 50
        self.r3.width = 15

        self.assertEqual(self.r1.width, 50)
        self.assertEqual(self.r3.width, 15)

        self.assertRaises(TypeError, Rectangle, "2", 4)
        self.assertRaises(TypeError, Rectangle, 2.667, 4)
        self.assertRaises(TypeError, Rectangle, True, 4)
        self.assertRaises(TypeError, Rectangle, [2], 4)
        self.assertRaises(TypeError, Rectangle, (2,), 4)
        self.assertRaises(TypeError, Rectangle, None, 4)

        self.assertRaises(ValueError, Rectangle, 0, 4)
        self.assertRaises(ValueError, Rectangle, -2, 5)

    def test_height(self):

        self.assertEqual(self.r1.height, 20)
        self.assertEqual(self.r2.height, 15)

        self.r1.height = 70
        self.r3.height = 35

        self.assertEqual(self.r1.height, 70)
        self.assertEqual(self.r3.height, 35)

        self.assertRaises(TypeError, Rectangle, 2, "4")
        self.assertRaises(TypeError, Rectangle, 2, 4.6554)
        self.assertRaises(TypeError, Rectangle, 2, True)
        self.assertRaises(TypeError, Rectangle, 2, [4])
        self.assertRaises(TypeError, Rectangle, 2, (4,))
        self.assertRaises(TypeError, Rectangle, 2, None)

        self.assertRaises(ValueError, Rectangle, 2, 0)
        self.assertRaises(ValueError, Rectangle, 2, -5)

if __name__ == '__main__':
    unittest.main()
