#!/usr/bin/python3
"""Module for testing `Square` class"""


from io import StringIO
import sys
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    '''
        Testing Square
    '''

    def setUp(self):
        '''
            Initializing instance with size and height
            parameters
        '''
        self.r = Square(5)
        self.r1 = Square(1,2,3,4)

    def tearDown(self):
        '''
            Deleting created instance
        '''
        del self.r

    def test_size(self):
        """unittest for size instance of Square class"""
        self.assertEqual(5, self.r.size)
        with self.assertRaises(TypeError):
            Square('5', self.r.size)
        with self.assertRaises(TypeError):
            Square(True, self.r.size)
        with self.assertRaises(TypeError):
            Square([3], self.r.size)
        with self.assertRaises(ValueError):
            Square(-5, self.r.size)

    def test_x(self):
        """unittest for x instance of Square class"""
        self.assertEqual(2, self.r1.x)
        with self.assertRaises(TypeError):
            Square('5', self.r1.x)
        with self.assertRaises(TypeError):
            Square(True, self.r1.x)
        with self.assertRaises(TypeError):
            Square([3], self.r1.x)
        with self.assertRaises(ValueError):
            Square(-5, self.r1.x)
        with self.assertRaises(ValueError):
            Square(0, self.r1.x)
    def test_y(self):
        """unittest for y instance of Square class"""
        self.assertEqual(3, self.r1.y)
        with self.assertRaises(TypeError):
            Square('4', self.r1.y)
        with self.assertRaises(TypeError):
            Square(True, self.r1.y)
        with self.assertRaises(TypeError):
            Square([4], self.r1.y)
        with self.assertRaises(ValueError):
            Square(-4, self.r1.y)
        with self.assertRaises(ValueError):
            Square(0, self.r1.y)

    def test_area(self):
        """unittest for area of a Square"""
        self.assertEqual(25, self.r.area())

    def test_str(self):
        """unittest for the string representation of Square class"""
        self.assertEqual("[Square] (4) 2/3 - 1", self.r1.__str__())

    def test_display_exc_xy(self):
        """unittest for display method without x and y"""
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1 = Square(3)
        r1.display()
        sys.stdout = sys.__stdout__
        output = ("###\n" +
                  "###\n" +
                  "###\n")
        self.assertEqual(capturedOutput.getvalue(), output)
    def test_display_x(self):
        """unittest for display method without x"""
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r2 = Square(10, 3)
        r2.display()
        sys.stdout = sys.__stdout__
        output1 = ("   ##########\n" +
                  "   ##########\n" +
                  "   ##########\n" +
                  "   ##########\n" +
                  "   ##########\n" +
                  "   ##########\n" +
                  "   ##########\n" +
                  "   ##########\n" +
                  "   ##########\n" +
                  "   ##########\n")
        self.assertEqual(capturedOutput.getvalue(), output1)
    def test_display_y(self):
        """unittest for display method without y"""
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r3 = Square(10, 0, 2)
        r3.display()
        sys.stdout = sys.__stdout__
        output2 = ("\n\n" +
                "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n")
        self.assertEqual(capturedOutput.getvalue(), output2)
    def test_display(self):
        """unittest for display method"""
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r = Square(10, 3, 2)
        r.display()
        sys.stdout = sys.__stdout__
        output = ("\n\n" +
                "   ##########\n" +
                  "   ##########\n" +
                  "   ##########\n" +
                  "   ##########\n" +
                  "   ##########\n" +
                  "   ##########\n" +
                  "   ##########\n" +
                  "   ##########\n" +
                  "   ##########\n" +
                  "   ##########\n")
        self.assertEqual(capturedOutput.getvalue(), output)

    def test_dictionary(self):
        """unittest for to_dictionary method"""
        dic = {'id':4,
                'x':2,
                'size':1,
                'y':3,
                }
        self.assertEqual(dic, self.r1.to_dictionary())

    def test_update(self):
        """test for update method"""
        self.r.update(7)
        self.assertEqual(7, self.r.id)
        self.r.update(7, 5)
        self.assertEqual(5, self.r.size)
        self.r.update(7, 5, 2)
        self.assertEqual(2, self.r.x)
        self.r.update(7, 5, 2, 4)
        self.assertEqual(4, self.r.y)

    def test_create(self):
        """test for create method"""
        self.r = Square.create(**{'id':89})
        self.assertEqual(89, self.r.id)
        self.r = Square.create(**{'id':89, 'size':1})
        self.assertEqual(1, self.r.size)
        self.r = Square.create(**{'id':89, 'size':1, 'x':30})
        self.assertEqual(30, self.r.x)
        self.r = Square.create(**{'id':89, 'size':1, 'x':3, 'y':90})
        self.assertEqual(90, self.r.y)

    def test_save_to_file(self):
        """test for save_to_file method"""
        r = Square.save_to_file(None)
        with open('Square.json', 'r') as f:
            self.assertEqual('[]', f.read())
        r = Square.save_to_file([])
        with open('Square.json', 'r') as f:
            self.assertEqual('[]', f.read())
        r = Square.save_to_file([Square(1)])
        with open('Square.json', 'r') as f:
            self.assertEqual('[{"id": 18, "x": 0, "size": 1, "y": 0}]', f.read())

    def test_load_from_file(self):
        """"test for load_from_file method"""
        
if __name__ == '__main__':
    unittest.main()
