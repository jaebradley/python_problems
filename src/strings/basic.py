"""
Basic string problems
"""

from collections import Counter
from itertools import chain
import string


def alphabetize(value):
    """
    Take a string and return all input characters in alphabetical order.
    Assume that no numbers or punctuation will be used.
    For the same character, uppercase characters should be returned before lowercase characters.
    Do not use the `sorted` helper method.
    Do not use any libraries that are not included with Python 3.6.1

    Args:
        value (str): the string value to alphabetize
    Returns:
        the input string with the characters in alphabetical order
    """

    counts = Counter(value)

    return ''.join(
        char * counts[char]
        for char in chain(*zip(string.ascii_uppercase, string.ascii_lowercase))
    )
