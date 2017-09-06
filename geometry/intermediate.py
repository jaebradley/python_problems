class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class LineSegment:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def do_line_segments_intersect(line_segment_1, line_segment_2):
    """
    Checks to see if two line segments have at least one point that they share.

    Let's call the ends of line_segment_1, A and B, and the ends of line_segment_2, C and D.
    Imagine standing at A and looking at B - if line_segment_2 intersects then either

    1. C or D is clockwise of line_segment_1 and the other end is counterclockwise. In other words,
       if C is "left" of the line segment then D is to the "right" and vice versa.
    2. C and/or D is on line_segment_1

    https://www.quora.com/Given-four-Cartesian-coordinates-how-do-I-check-whether-these-two-segments-intersect-or-not-using-C-C++
    """

    # Get the relative orientation of each line segment's end with the other line segment
    segment_2_start_orientation = calculate_point_triplet_orientation(line_segment_1.start, line_segment_1.end, line_segment_2.start)
    segment_2_end_orientation = calculate_point_triplet_orientation(line_segment_1.start, line_segment_1.end, line_segment_2.end)
    segment_1_start_orientation = calculate_point_triplet_orientation(line_segment_2.start, line_segment_2.end, line_segment_1.start)
    segment_1_end_orientation = calculate_point_triplet_orientation(line_segment_2.start, line_segment_2.end, line_segment_1.end)

    # If each segment has at least one end that is clockwise relative to the other end
    # then the product of each segment's orientation value should be negative
    segment_2_has_one_clockwise_end = segment_2_start_orientation * segment_2_end_orientation < 0
    segment_1_has_one_clockwise_end = segment_1_start_orientation * segment_1_end_orientation < 0

    if segment_2_has_one_clockwise_end and segment_1_has_one_clockwise_end:
        return True

    # The only other intersection case is if at least one end of one of the line segments lies on the other.
    # In this case, one of the ends would be collinear. Now, we would just check to see if any end could
    # potentially lie on the other segment.

    is_any_end_collinear = segment_2_start_orientation * segment_2_end_orientation * segment_1_start_orientation * segment_1_end_orientation == 0

    could_segment_1_contain_segment_2_start = could_line_segment_contain_coordinate(line_segment_1, line_segment_2.start)
    could_segment_1_contain_segment_2_end = could_line_segment_contain_coordinate(line_segment_1, line_segment_2.end)
    could_segment_2_contain_segment_1_start = could_line_segment_contain_coordinate(line_segment_2, line_segment_1.start)
    could_segment_2_contain_segment_1_end = could_line_segment_contain_coordinate(line_segment_2, line_segment_1.end)
    return is_any_end_collinear and \
           (
               could_segment_1_contain_segment_2_start or could_segment_1_contain_segment_2_end or
               could_segment_2_contain_segment_1_start or could_segment_2_contain_segment_1_end
           )


def calculate_point_triplet_orientation(coordinate_1, coordinate_2, coordinate_3):
    """
    Returns a value that represents the negative sine of the angle created by connecting connecting coordinate_1 to
    coordinate_2 to coordinate_3.

    If this connection occurs in a clockwise fashion the value will be negative, counterclockwise will be positive,
    and collinear will be 0.

    This is equivalent to taking the cross-product of the vectors created by the first and second coordinates and
    the second and third coordinates.

    https://en.oxforddictionaries.com/definition/point_triplet
    """
    return (coordinate_2.x - coordinate_1.x) * (coordinate_3.y - coordinate_1.y) - (coordinate_2.y - coordinate_1.y) * (coordinate_3.x - coordinate_1.x)


def could_line_segment_contain_coordinate(line_segment, coordinate):
    """
    Checks to see if a line segment could contain a coordinate by seeing if the coordinate's values are between the
    line segment's start and end coordinate values.
    """
    return ((line_segment.start.x <= coordinate.x <= line_segment.end.x) or (line_segment.end.x >= coordinate.x >= line_segment.start.x)) and \
           ((line_segment.start.y <= coordinate.y <= line_segment.end.y) or (line_segment.end.y >= coordinate.y >= line_segment.start.y))
