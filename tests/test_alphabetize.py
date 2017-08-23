from unittest import TestCase

from src.alphabetize import alphabetize


class TestAlphabetize(TestCase):
    def test_should_return_alphabetized_string(self):
        self.assertEqual('eHLlo', alphabetize('HelLo'))
