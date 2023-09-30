#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_one_element_list(self):
        self.assertEqual(max_integer([42]), 42)

    def test_list_with_duplicates(self):
        self.assertEqual(max_integer([1, 2, 3, 3]), 3)

    def test_sorted_descending_list(self):
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_sorted_ascending_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_unsorted_list(self):
        self.assertEqual(max_integer([3, 7, 2, 1, 9, 8, 6]), 9)

    def test_list_with_negative_numbers(self):
        self.assertEqual(max_integer([-5, -2, 0, 4, -8]), 4)
if __name__ == '__main__':
    unittest.main()
