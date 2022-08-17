#!/usr/bin/python3
"""Module for testing `rectangle` class"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """class: RectangleTest"""
    def test_initialization(self):
        r1 = Rectangle(2,5)
        self.assertEqual(r1.id, Rectangle._Base__nb_objects)
        r2 = Rectangle(1,2)
        self.assertEqual(r2.id, Rectangle._Base__nb_objects)

if __name__ == '__main__':
    unittest.main()
