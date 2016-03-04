import unittest
import random

from ..point import Point


class TestPointClass(unittest.TestCase):
    def setUp(self):
        pass

    def coordinates_properly_set(self, x, y):
        """
        This test checks if the Point constructor correctly
        assigns the x and y coordinates to the appropriate variables.
        """
        test_point = Point(x, y)
        self.assertEqual(test_point.x, x)
        self.assertEqual(test_point.y, y)

    def test_coincident(self):
        """
        This test checks if the is_coincident method works properly.
        """
        point_a = Point(10, 37)
        point_b = Point(10, 37)
        point_c = Point(10, 36)
        point_d = Point(0, 37)
        self.assertTrue(point_a.is_coincident(point_b))
        self.assertFalse(point_a.is_coincident(point_c))
        self.assertFalse(point_a.is_coincident(point_d))

    def test_shift(self):
        """
        This test checks if the shift_point method works properly.
        """
        test_point = Point(10, 37)
        test_point.shift_point(5, 10)
        self.assertEqual(test_point.x, 15)
        self.assertEqual(test_point.y, 47)

    def test_marking(self):
        """
        This test verifies that marked points can be created properly.
        """

        def get_occurrence_count(points, mark):
            """
            This is a helper method for test_marking.
            Returns the number of occurrences of a certain mark in a list of points.
            """
            return len(list(filter(lambda current_point: current_point.mark['color'] == mark, points)))

        random.seed(9631)
        marks = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
        points = []
        for i in range(20):
            points.append(Point(0, 0, color=random.choice(marks)))

        self.assertEqual(get_occurrence_count(points, 'red'), 5)
        self.assertEqual(get_occurrence_count(points, 'orange'), 1)
        self.assertEqual(get_occurrence_count(points, 'yellow'), 2)
        self.assertEqual(get_occurrence_count(points, 'green'), 3)
        self.assertEqual(get_occurrence_count(points, 'blue'), 1)
        self.assertEqual(get_occurrence_count(points, 'indigo'), 5)
        self.assertEqual(get_occurrence_count(points, 'violet'), 3)
