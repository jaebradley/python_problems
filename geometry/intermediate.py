class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class LineSegment:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def do_line_segments_intersect(line_segment_1, line_segment_2):
    line_segment_2_start_orientation_relative_to_line_segment_1 = calculate_point_triplet_orientation(line_segment_1.start, line_segment_1.end, line_segment_2.start)
    line_segment_2_end_orientation_relative_to_line_segment_1 = calculate_point_triplet_orientation(line_segment_1.start, line_segment_1.end, line_segment_2.end)
    line_segment_1_start_orientation_relative_to_line_segment_2 = calculate_point_triplet_orientation(line_segment_2.start, line_segment_2.end, line_segment_1.start)
    line_segment_1_end_orientation_relative_to_line_segment_2 = calculate_point_triplet_orientation(line_segment_2.start, line_segment_2.end, line_segment_1.end)

    does_line_segment_2_have_one_end_clockwise_to_line_segment_1 = line_segment_2_start_orientation_relative_to_line_segment_1 * line_segment_2_end_orientation_relative_to_line_segment_1 < 0
    does_line_segment_1_have_one_end_clockwise_to_line_segment_2 = line_segment_1_start_orientation_relative_to_line_segment_2 * line_segment_1_end_orientation_relative_to_line_segment_2 < 0

    if does_line_segment_2_have_one_end_clockwise_to_line_segment_1 and does_line_segment_1_have_one_end_clockwise_to_line_segment_2:
        return True

    is_one_end_point_collinear = line_segment_2_start_orientation_relative_to_line_segment_1 * line_segment_2_end_orientation_relative_to_line_segment_1 * line_segment_1_start_orientation_relative_to_line_segment_2 * line_segment_1_end_orientation_relative_to_line_segment_2 == 0

    return is_one_end_point_collinear and \
           (does_line_segment_contain_coordinate(line_segment_1, line_segment_2.start) or
            does_line_segment_contain_coordinate(line_segment_1, line_segment_2.end))


def calculate_point_triplet_orientation(coordinate_1, coordinate_2, coordinate_3):
    return (coordinate_2.x - coordinate_1.x) * (coordinate_3.y - coordinate_1.y) - (coordinate_2.y - coordinate_1.y) * (coordinate_3.x - coordinate_1.x)


def does_line_segment_contain_coordinate(line_segment, coordinate):
    return ((line_segment.start.x <= coordinate.x <= line_segment.end.x) or (line_segment.end.x >= coordinate.x >= line_segment.start.x)) and \
           ((line_segment.start.y <= coordinate.y <= line_segment.end.y) or (line_segment.end.y >= coordinate.y >= line_segment.start.y))
