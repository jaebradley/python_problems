"""
Unit Test for strings.basic problems
"""

from unittest import TestCase

from src.strings.basic import alphabetize


class TestAlphabetize(TestCase):
    """
    Unit Test for alphabetize method
    """

    def test_should_return_alphabet(self):
        """
        Test alphabetize method using every uppercase and lowercase character
        """
        self.assertEqual('aBbcDeFgHiJkLmNoPqRsTuVwXyZ', alphabetize('ZyXwVuTsRqPoNmLkJiHgFeDcBba'))
