#!/usr/bin/python3
"""This is a unit test module for the Square class
that inherits from the Rectangle class"""

import unittest
from models.square import Square
from models.base import Base

class TestSquare(unittest.TestCase):
    """Test class for the Square class"""

    def setUp(self):
        """set up sample square objects"""

        Base._Base__nb_objects = 0
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

        self.assertRaises(ValueError, Square, 0)
        self.assertRaises(ValueError, Square, -1)

    def test_size(self):
        """test size attribute of a square instance"""

        self.assertEqual(self.s1.size, 5)

        self.s1.size = 10

        self.assertEqual(self.s1.size, 10)
        with self.assertRaises(TypeError):
            self.s1.size = True

        with self.assertRaises(TypeError):
            self.s1.size = "10"

        with self.assertRaises(ValueError):
            self.s1.size = -1

        with self.assertRaises(ValueError):
            self.s1.size = 0

    
    def test_area(self):
        """test area method of a square instance"""

        self.assertEqual(self.s1.area(), 25)
        self.assertEqual(self.s3.area(), 16)

    def test_y(self):
        """test y attribute of a square instance"""

        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s3.y, 6)
        self.assertEqual(self.s4.x, 4)

        self.assertRaises(TypeError, Square, 2, 2, 3.2)
        self.assertRaises(TypeError, Square, 2, 2, True)
        self.assertRaises(TypeError, Square, 2, 2, [3])
        self.assertRaises(TypeError, Square, 2, 2, (3,))
        self.assertRaises(TypeError, Square, 2, 2, None)
        self.assertRaises(TypeError, Square, 2, 2, "3")

        self.assertRaises(ValueError, Square, 2, 2, -1)

    def test_x(self):
        """test x attribute of a square instance"""

        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s3.x, 2)
        self.assertEqual(self.s4.x, 4)

        self.assertRaises(TypeError, Square, 2, 3.2)
        self.assertRaises(TypeError, Square, 2, True)
        self.assertRaises(TypeError, Square, 2, [3])
        self.assertRaises(TypeError, Square, 2, (3,))
        self.assertRaises(TypeError, Square, 2, None)
        self.assertRaises(TypeError, Square, 2, "3")

        self.assertRaises(ValueError, Square, 2, -1)
