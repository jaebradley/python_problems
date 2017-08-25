"""
Basic geometric problems
"""


class Triangle:
    def __init__(self, longest_side, middle_side, shortest_side):
        self.longest_side = longest_side
        self.middle_side = middle_side
        self.shortest_side = shortest_side

    def __eq__(self, other):
        """Override the default Equals behavior"""
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __ne__(self, other):
        """Define a non-equality test"""
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        """Override the default hash behavior (that returns the id or the object)"""
        return hash(tuple(sorted(self.__dict__.items())))


def identify_maximum_perimeter_triangle(values):
    """
    Given an array of integer values, identify the three values that can create the triangle with the largest perimeter.
    In the case of multiple triangles with the same perimeter, choose the one with the longest side. In the case of a
    tie, choose one with the longest minimum side.
    :param values: an array of integer values
    :return: A Triangle with each of the sides defined, None if no Triangle can be constructed, and raises a ValueError
             if the input array has less than three values
    """
    if len(values) < 3:
        raise ValueError('Unable to identify triangle with less than three values')

    sorted_values = sorted(values)

    for index in range(len(sorted_values) - 1, 1, -1):
        if sorted_values[index] < sorted_values[index - 1] + sorted_values[index - 2]:
            return Triangle(
                    longest_side=sorted_values[index], middle_side=sorted_values[index - 1], shortest_side=sorted_values[index - 2])

    return None
