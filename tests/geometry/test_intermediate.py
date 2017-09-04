"""
Unit Test for geometry.intermediate problems
"""

from unittest import TestCase

from geometry.intermediate import Coordinate, LineSegment, do_line_segments_intersect


class TestLineSegmentsIntersection(TestCase):
    """
    Unit Test for identifying if two line segments intersect
    """
    def test_line_segments_intersect(self):
        horizontal_line_segment_start = Coordinate(-1, 0)
        horizontal_line_segment_end = Coordinate(1, 0)
        horizontal_line_segment = LineSegment(horizontal_line_segment_start, horizontal_line_segment_end)

        vertical_line_segment_start = Coordinate(0, 1)
        vertical_line_segment_end = Coordinate(0, -1)
        vertical_line_segment = LineSegment(vertical_line_segment_start, vertical_line_segment_end)

        self.assertTrue(do_line_segments_intersect(horizontal_line_segment, vertical_line_segment))

    def test_line_segments_do_not_intersect(self):
        horizontal_line_segment_start = Coordinate(-1, 0)
        horizontal_line_segment_end = Coordinate(1, 0)
        horizontal_line_segment = LineSegment(horizontal_line_segment_start, horizontal_line_segment_end)

        vertical_line_segment_start = Coordinate(0, 2)
        vertical_line_segment_end = Coordinate(0, 1)
        vertical_line_segment = LineSegment(vertical_line_segment_start, vertical_line_segment_end)

        self.assertFalse(do_line_segments_intersect(horizontal_line_segment, vertical_line_segment))

    def test_line_segments_do_not_intersect_with_same_slope(self):
        horizontal_line_segment_start = Coordinate(-1, 0)
        horizontal_line_segment_end = Coordinate(1, 0)
        horizontal_line_segment = LineSegment(horizontal_line_segment_start, horizontal_line_segment_end)

        vertical_line_segment_start = Coordinate(3, 0)
        vertical_line_segment_end = Coordinate(4, 0)
        vertical_line_segment = LineSegment(vertical_line_segment_start, vertical_line_segment_end)

        self.assertFalse(do_line_segments_intersect(horizontal_line_segment, vertical_line_segment))