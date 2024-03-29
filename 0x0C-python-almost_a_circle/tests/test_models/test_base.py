#!/usr/bin/python3
"""Unittests for base
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Define unit test for Base model"""

    def test_initialization(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 2)
        self.assertEqual(base2.id, 3)

    def test_saving_id(self):
        base = Base(100)
        self.assertEqual(base.id, 100)

    def test_to_json_string_valid(self):
        base = Base()
        self.assertEqual(base.to_json_string(None), '[]')
        self.assertEqual(base.to_json_string([]), '[]')
        self.assertEqual(base.to_json_string([{'id':2}]), '[{"id": 2}]')

    def test_from_json_string_valid(self):
        base = Base()
        self.assertEqual(base.from_json_string(None), [])
        self.assertEqual(base.from_json_string([]), [])
        self.assertEqual(base.from_json_string('[{"id":89}]'), [{'id':89}])

if __name__ == '__main__':
    unittest.main()
