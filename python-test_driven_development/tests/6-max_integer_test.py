#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):
    """Tests for max_integer."""
    def test_ordered(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
    def test_unordered(self):
        self.assertEqual(max_integer([1, 3, 2]), 3)
    def test_empty(self):
        self.assertEqual(max_integer([]), None)
    def test_negative(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)
    def test_max_at_beginning(self):
        self.assertEqual(max_integer([10, 1, 2]), 10)
    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.7, 0.5]), 2.7)
