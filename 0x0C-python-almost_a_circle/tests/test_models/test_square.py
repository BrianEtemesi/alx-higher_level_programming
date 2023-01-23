#!/usr/bin/python3
"""This is a unit test module for the Square class
that inherits from the Rectangle class"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test class for the Square class"""

    def setUp(self):
        """set up sample square objects"""

        self.s1 = Square(5)
        self.s2 = Square(10, id=100)
        self.s3 = Square(4, 2, 6, 200)
        self.s4 = Square(10, 4, 4)

    def test_id(self):
        """test the id attribute of a square instance"""

        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, 100)
        self.assertEqual(self.s3.id, 200)
        self.assertEqual(self.s4.id, 2)

    def test_width(self):
        """tests the width attribute of the square"""

        self.assertEqual(self.s1.width, 5)
        self.assertEqual(self.s2.width, 10)

        self.s2.width = 11

        self.assertEqual(self.s2.width, 11)

        self.assertRaises(TypeError, Square, 5.4)
        self.assertRaises(TypeError, Square, True)
        self.assertRaises(TypeError, Square, [2])
        self.assertRaises(TypeError, Square, (2,))
        self.assertRaises(TypeError, Square, None)
        self.assertRaises(TypeError, Square, "2")
