"""
Unit Test for geometry.intermediate problems
"""

from unittest import TestCase

from geometry.intermediate import Coordinate, LineSegment, do_line_segments_intersect


class TestLineSegmentsIntersection(TestCase):
    """
    Unit Test for identifying if two line segments intersect
    """
    def test_axis_line_segments_intersect(self):
        line_segment_1_start = Coordinate(-1, 0)
        line_segment_1_end = Coordinate(1, 0)
        line_segment_1 = LineSegment(line_segment_1_start, line_segment_1_end)

        line_segment_2_start = Coordinate(0, 1)
        line_segment_2_end = Coordinate(0, -1)
        line_segment_2 = LineSegment(line_segment_2_start, line_segment_2_end)

        self.assertTrue(do_line_segments_intersect(line_segment_1, line_segment_2))

    def test_line_segments_do_not_intersect(self):
        line_segment_1_start = Coordinate(-1, 0)
        line_segment_1_end = Coordinate(1, 0)
        line_segment_1 = LineSegment(line_segment_1_start, line_segment_1_end)

        line_segment_2_start = Coordinate(0, 2)
        line_segment_2_end = Coordinate(0, 1)
        line_segment_2 = LineSegment(line_segment_2_start, line_segment_2_end)

        self.assertFalse(do_line_segments_intersect(line_segment_1, line_segment_2))

    def test_line_segments_do_not_intersect_with_same_slope(self):
        line_segment_1_start = Coordinate(-1, 0)
        line_segment_1_end = Coordinate(1, 0)
        line_segment_1 = LineSegment(line_segment_1_start, line_segment_1_end)

        line_segment_2_start = Coordinate(3, 0)
        line_segment_2_end = Coordinate(4, 0)
        line_segment_2 = LineSegment(line_segment_2_start, line_segment_2_end)

        self.assertFalse(do_line_segments_intersect(line_segment_1, line_segment_2))

    def test_collinear_overlapping_line_segments_intersect(self):
        line_segment_1_start = Coordinate(-1, 0)
        line_segment_1_end = Coordinate(1, 0)
        line_segment_1 = LineSegment(line_segment_1_start, line_segment_1_end)

        line_segment_2_start = Coordinate(0, 0)
        line_segment_2_end = Coordinate(4, 0)
        line_segment_2 = LineSegment(line_segment_2_start, line_segment_2_end)

        self.assertTrue(do_line_segments_intersect(line_segment_1, line_segment_2))

    def test_parallel_line_segments_do_not_intersect(self):
        line_segment_1_start = Coordinate(-1, 0)
        line_segment_1_end = Coordinate(1, 0)
        line_segment_1 = LineSegment(line_segment_1_start, line_segment_1_end)

        line_segment_2_start = Coordinate(-1, 1)
        line_segment_2_end = Coordinate(1, 1)
        line_segment_2 = LineSegment(line_segment_2_start, line_segment_2_end)

        self.assertFalse(do_line_segments_intersect(line_segment_1, line_segment_2))
