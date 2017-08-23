from unittest import TestCase

from src.strings.basic import alphabetize


class TestAlphabetize(TestCase):
    def test_should_return_alphabetically_ordered_string(self):
        self.assertEqual('eHLlo', alphabetize('HelLo'))

    def test_should_return_alphabet(self):
        self.assertEqual('aBcDeFgHiJkLmNoPqRsTuVwXyZ', alphabetize('ZyXwVuTsRqPoNmLkJiHgFeDcBa'))
