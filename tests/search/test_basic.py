"""
Unit Test for search.basic problems
"""

from unittest import TestCase

from search.basic import Node, depth_first_search


class TestDepthFirstSearch(TestCase):
    """
    Unit Test for Depth First Search implementation
    """
    def test_search_value_exists(self):
        """Test returns True"""
        f = Node(value='F', children={})
        e = Node(value='E', children={f})
        c = Node(value='C', children={f})
        d = Node(value='D', children={})
        b = Node(value='B', children={d, e})
        a = Node(value='A', children={b, c})

        self.assertTrue(depth_first_search(root=a, target='F'))

    def test_search_value_does_not_exist(self):
        """Test returns True"""
        f = Node(value='F', children={})
        e = Node(value='E', children={f})
        c = Node(value='C', children={f})
        d = Node(value='D', children={})
        b = Node(value='B', children={d, e})
        a = Node(value='A', children={b, c})

        self.assertFalse(depth_first_search(root=a, target='J'))