"""
Unit Test for geometry.basic problems
"""

from unittest import TestCase

from geometry.basic import identify_maximum_perimeter_triangle, Triangle


class TestIdentifyMaximumPerimeterTriangle(TestCase):
    """
    Unit Test for identify maximum perimeter triangle method
    """
    def test_maximum_perimeter_triangle_exists(self):
        """Test returns the expected triangle"""
        expected = Triangle(longest_side=3, middle_side=3, shortest_side=2)
        self.assertEqual(expected, identify_maximum_perimeter_triangle([3, 9, 2, 15, 3]))

    def test_maximum_perimeter_triangle_does_not_exist(self):
        """Test returns None when a triangle cannot be identified"""
        self.assertIsNone(identify_maximum_perimeter_triangle([1, 2, 3]))

    def test_exception_thrown(self):
        """Test raises an error when the input values are invalid"""
        self.assertRaises(ValueError, identify_maximum_perimeter_triangle, [])