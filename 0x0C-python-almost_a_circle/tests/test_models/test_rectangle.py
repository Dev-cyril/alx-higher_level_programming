#!/usr/bin/python3
"""Module for testing `rectangle` class"""


from io import StringIO
import sys
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    '''
        Testing rectangle
    '''

    def setUp(self):
        '''
            Initializing instance with width and height
            parameters
        '''
        self.r = Rectangle(5, 10)
        self.r1 = Rectangle(1,2,3,4,5)

    def tearDown(self):
        '''
            Deleting created instance
        '''
        del self.r

    def test_width(self):
        """unittest for width instance of rectangle class"""
        self.assertEqual(5, self.r.width)
    def test_width2(self):
        with self.assertRaises(TypeError):
            Rectangle('5', self.r.width)
    def test_width3(self):
        with self.assertRaises(ValueError):
            Rectangle(-5, self.r.width)
    
    def test_height(self):
        """unittest for height instance of rectangle class"""
        self.assertEqual(10, self.r.height)
    def test_height2(self):
        with self.assertRaises(TypeError):
            Rectangle('5', self.r.height)
    def test_height3(self):
        with self.assertRaises(ValueError):
            Rectangle(-5, self.r.height)

    def test_x(self):
        """unittest for x instance of rectangle class"""
        self.assertEqual(3, self.r1.x)
    def test_x2(self):
        with self.assertRaises(TypeError):
            Rectangle('5', self.r1.x)
    def test_x3(self):
        with self.assertRaises(ValueError):
            Rectangle(-5, self.r1.x)
    def test_x4(self):
        with self.assertRaises(ValueError):
            Rectangle(0, self.r1.x)
    def test_y(self):
        """unittest for y instance of rectangle class"""
        self.assertEqual(4, self.r1.y)
    def test_y2(self):
        with self.assertRaises(TypeError):
            Rectangle('4', self.r1.y)
    def test_y3(self):
        with self.assertRaises(ValueError):
            Rectangle(-4, self.r1.y)
    def test_y4(self):
        with self.assertRaises(ValueError):
            Rectangle(0, self.r1.y)

    def test_area(self):
        """unittest for area of a rectangle"""
        self.assertEqual(50, self.r.area())

    def test_str(self):
        """unittest for the string representation of rectangle class"""
        self.assertEqual("[Rectangle] (5) 3/4 - 1/2", self.r1.__str__())

    def test_display_exc_xy(self):
        """unittest for display method without x and y"""
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1 = Rectangle(10, 4)
        r1.display()
        sys.stdout = sys.__stdout__
        output = ("##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n")
        self.assertEqual(capturedOutput.getvalue(), output)
    def test_display_x(self):
        """unittest for display method without x"""
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r2 = Rectangle(10, 4, 3)
        r2.display()
        sys.stdout = sys.__stdout__
        output1 = ("   ##########\n" +
                  "   ##########\n" +
                  "   ##########\n" +
                  "   ##########\n")
        self.assertEqual(capturedOutput.getvalue(), output1)
    def test_display_y(self):
        """unittest for display method without y"""
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r3 = Rectangle(10, 4, 0, 2)
        r3.display()
        sys.stdout = sys.__stdout__
        output2 = ("\n\n" +
                "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n")
        self.assertEqual(capturedOutput.getvalue(), output2)
    def test_display(self):
        """unittest for display method without y"""
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r = Rectangle(10, 4, 3, 2)
        r.display()
        sys.stdout = sys.__stdout__
        output = ("\n\n" +
                "   ##########\n" +
                  "   ##########\n" +
                  "   ##########\n" +
                  "   ##########\n")
        self.assertEqual(capturedOutput.getvalue(), output)

    def test_dictionary(self):
        """unittest for to_dictionary method"""
        dic = {'x':3,
                'y':4,
                'id':5,
                'height':2,
                'width':1}
        self.assertEqual(dic, self.r1.to_dictionary())

    def test_update(self):
        """test for update method"""
        self.r.update(7)
        self.assertEqual(7, self.r.id)
        self.r.update(7, 5)
        self.assertEqual(5, self.r.width)
        self.r.update(7, 5, 6)
        self.assertEqual(6, self.r.height)
        self.r.update(7, 5, 6, 2)
        self.assertEqual(2, self.r.x)
        self.r.update(7, 5, 6, 2, 4)
        self.assertEqual(4, self.r.y)

    def test_create(self):
        """test for create method"""
        self.r = Rectangle.create(**{'id':89})
        self.assertEqual(89, self.r.id)
        self.r = Rectangle.create(**{'id':89, 'width':1})
        self.assertEqual(1, self.r.width)
        self.r = Rectangle.create(**{'id':89, 'width':1, 'height':20})
        self.assertEqual(20, self.r.height)
        self.r = Rectangle.create(**{'id':89, 'width':1, 'height':2, 'x':30})
        self.assertEqual(30, self.r.x)
        self.r = Rectangle.create(**{'id':89, 'width':1, 'height':2, 'x':3, 'y':90})
        self.assertEqual(90, self.r.y)

    def test_save_to_file(self):
        """test for save_to_file method"""
        r = Rectangle.save_to_file(None)
        with open('Rectangle.json', 'r') as f:
            self.assertEqual('[]', f.read())
    def test_save_to_file2(self):    
        r = Rectangle.save_to_file([])
        with open('Rectangle.json', 'r') as f:
            self.assertEqual('[]', f.read())
    def test_save_to_file3(self):
        r = Rectangle.save_to_file([Rectangle(1, 6)])
        with open('Rectangle.json', 'r') as f:
            self.assertEqual('[{"x": 0, "y": 0, "id": 30, "height": 6, "width": 1}]', f.read())

    def test_load_from_file(self):
        """"test for load_from_file method"""

if __name__ == '__main__':
    unittest.main()
