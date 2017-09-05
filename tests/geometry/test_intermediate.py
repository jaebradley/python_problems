"""
Unit Test for geometry.intermediate problems
"""

from unittest import TestCase

from geometry.intermediate import Coordinate, LineSegment, do_line_segments_intersect, \
    could_line_segment_contain_coordinate, calculate_point_triplet_orientation


class TestLineSegmentsIntersection(TestCase):
    """
    Unit Test for identifying if two line segments intersect
    """
    def test_proper_line_segments_intersect(self):
        """
        Tests that two proper line segments which intersect, returns True
        """
        line_segment_1_start = Coordinate(-1, 0)
        line_segment_1_end = Coordinate(1, 0)
        line_segment_1 = LineSegment(line_segment_1_start, line_segment_1_end)

        line_segment_2_start = Coordinate(0, 1)
        line_segment_2_end = Coordinate(0, -1)
        line_segment_2 = LineSegment(line_segment_2_start, line_segment_2_end)

        self.assertTrue(do_line_segments_intersect(line_segment_1, line_segment_2))
        self.assertTrue(do_line_segments_intersect(line_segment_2, line_segment_1))

    def test_line_segments_do_not_intersect(self):
        """
        Tests that two line segments which never intersect, returns False
        """
        line_segment_1_start = Coordinate(-1, 0)
        line_segment_1_end = Coordinate(1, 0)
        line_segment_1 = LineSegment(line_segment_1_start, line_segment_1_end)

        line_segment_2_start = Coordinate(0, 2)
        line_segment_2_end = Coordinate(0, 1)
        line_segment_2 = LineSegment(line_segment_2_start, line_segment_2_end)

        self.assertFalse(do_line_segments_intersect(line_segment_1, line_segment_2))
        self.assertFalse(do_line_segments_intersect(line_segment_2, line_segment_1))

    def test_collinear_overlapping_line_segments_intersect(self):
        """
        Tests that two line segments that are parallel and do intersect, returns True
        """
        line_segment_1_start = Coordinate(-1, 0)
        line_segment_1_end = Coordinate(1, 0)
        line_segment_1 = LineSegment(line_segment_1_start, line_segment_1_end)

        line_segment_2_start = Coordinate(0, 0)
        line_segment_2_end = Coordinate(4, 0)
        line_segment_2 = LineSegment(line_segment_2_start, line_segment_2_end)

        self.assertTrue(do_line_segments_intersect(line_segment_1, line_segment_2))
        self.assertTrue(do_line_segments_intersect(line_segment_2, line_segment_1))

    def test_parallel_line_segments_do_not_intersect(self):
        """
        Tests that two parallel line segments that do not intersect, returns False
        """
        line_segment_1_start = Coordinate(-1, 0)
        line_segment_1_end = Coordinate(1, 0)
        line_segment_1 = LineSegment(line_segment_1_start, line_segment_1_end)

        line_segment_2_start = Coordinate(-1, 1)
        line_segment_2_end = Coordinate(1, 1)
        line_segment_2 = LineSegment(line_segment_2_start, line_segment_2_end)

        self.assertFalse(do_line_segments_intersect(line_segment_1, line_segment_2))
        self.assertFalse(do_line_segments_intersect(line_segment_2, line_segment_1))


class TestCouldLineSegmentContainCoordinate(TestCase):
    """
    Unit Test for identifying if a line segment could contain a coordinate
    """

    def test_line_segment_could_contain_coordinate(self):
        """
        Tests that a line segment could contain a coordinate with valid x and y values
        """
        line_segment_1_start = Coordinate(-1, 0)
        line_segment_1_end = Coordinate(1, 0)
        line_segment_1 = LineSegment(line_segment_1_start, line_segment_1_end)
        coordinate = Coordinate(-1, 0)
        self.assertTrue(could_line_segment_contain_coordinate(line_segment_1, coordinate))

    def test_line_segment_could_not_contain_too_small_x_value_coordinate(self):
        """
        Tests that a line segment could not contain a coordinate with too small of an x value
        """
        line_segment_1_start = Coordinate(-1, 0)
        line_segment_1_end = Coordinate(1, 0)
        line_segment_1 = LineSegment(line_segment_1_start, line_segment_1_end)
        coordinate = Coordinate(-2, 0)
        self.assertFalse(could_line_segment_contain_coordinate(line_segment_1, coordinate))

    def test_line_segment_could_not_contain_too_large_x_value_coordinate(self):
        """
        Tests that a line segment could not contain a coordinate with too large of an x value
        """
        line_segment_1_start = Coordinate(-1, 0)
        line_segment_1_end = Coordinate(1, 0)
        line_segment_1 = LineSegment(line_segment_1_start, line_segment_1_end)
        coordinate = Coordinate(2, 0)
        self.assertFalse(could_line_segment_contain_coordinate(line_segment_1, coordinate))

    def test_line_segment_could_not_contain_too_small_y_value_coordinate(self):
        """
        Tests that a line segment could not contain a coordinate with too small of a y value
        """
        line_segment_1_start = Coordinate(-1, 0)
        line_segment_1_end = Coordinate(1, 0)
        line_segment_1 = LineSegment(line_segment_1_start, line_segment_1_end)
        coordinate = Coordinate(-1, -2)
        self.assertFalse(could_line_segment_contain_coordinate(line_segment_1, coordinate))

    def test_line_segment_could_not_contain_too_large_y_value_coordinate(self):
        """
        Tests that a line segment could not contain a coordinate with too large of a y value
        """
        line_segment_1_start = Coordinate(-1, 0)
        line_segment_1_end = Coordinate(1, 0)
        line_segment_1 = LineSegment(line_segment_1_start, line_segment_1_end)
        coordinate = Coordinate(-1, 2)
        self.assertFalse(could_line_segment_contain_coordinate(line_segment_1, coordinate))


class TestCalculatePointTripletOrientation(TestCase):
    """
    Unit Test for identifying the orientation value of a point triplet
    """

    def test_collinear_points(self):
        """
        Test that three points on the same line returns 0
        """
        point_1 = Coordinate(-1, -1)
        point_2 = Coordinate(0, 0)
        point_3 = Coordinate(1, 1)
        self.assertEqual(0, calculate_point_triplet_orientation(point_1, point_2, point_3))

    def test_clockwise_points(self):
        """
        Test that three points that form a right angle to the right returns -1
        """
        point_1 = Coordinate(0, -1)
        point_2 = Coordinate(0, 0)
        point_3 = Coordinate(1, 0)
        self.assertEqual(-1, calculate_point_triplet_orientation(point_1, point_2, point_3))

    def test_counterclockwise_points(self):
        """
        Test that three points that form a right angle to the left returns 1
        """
        point_1 = Coordinate(0, -1)
        point_2 = Coordinate(0, 0)
        point_3 = Coordinate(-1, 0)
        self.assertEqual(1, calculate_point_triplet_orientation(point_1, point_2, point_3))
