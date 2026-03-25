#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):
    """Test class for max_integer."""
    def test_basic(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
    def test_empty(self):
        self.assertEqual(max_integer([]), None)
    def test_negative(self):
        self.assertEqual(max_integer([-1, -5, -2]), -1)
    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)
