import enum


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class LineSegment:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class CrossProductType(enum.Enum):
    CLOCKWISE = 'clockwise'
    COUNTERCLOCKWISE = 'counterclockwise'
    COLLINEAR = 'collinear'


def do_line_segments_intersect(line_segment_1, line_segment_2):
    a = identify_cross_product_type(line_segment_1.start, line_segment_1.end, line_segment_2.start)
    b = identify_cross_product_type(line_segment_1.start, line_segment_1.end, line_segment_2.end)
    c = identify_cross_product_type(line_segment_2.start, line_segment_2.end, line_segment_1.start)
    d = identify_cross_product_type(line_segment_2.start, line_segment_2.end, line_segment_1.end)

    if CrossProductType.CLOCKWISE in [a, b] and CrossProductType.CLOCKWISE in [c, d]:
        return True

    return CrossProductType.COLLINEAR in [a, b, c, d] and \
           (is_coordinate_on_line_segment(line_segment_1, line_segment_2.start) or
            is_coordinate_on_line_segment(line_segment_1, line_segment_2.end))


def identify_cross_product_type(coordinate_1, coordinate_2, coordinate_3):
    value = (coordinate_2.x - coordinate_1.x) * (coordinate_3.y - coordinate_1.y) - (coordinate_2.y - coordinate_1.y) * (coordinate_3.x - coordinate_1.x)
    if value > 0:
        return CrossProductType.COUNTERCLOCKWISE

    elif value < 0:
        return CrossProductType.CLOCKWISE

    return CrossProductType.COLLINEAR


def is_coordinate_on_line_segment(line_segment, coordinate):
    return ((line_segment.start.x <= coordinate.x <= line_segment.end.x) or (line_segment.end.x >= coordinate.x >= line_segment.start.x)) \
        and ((line_segment.start.y <= coordinate.y <= line_segment.end.y) or (line_segment.end.y >= coordinate.y >= line_segment.start.y)) \



