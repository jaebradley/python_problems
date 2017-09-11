"""
Unit Test for search.basic problems
"""

from unittest import TestCase

from search.basic import recursive_dfs, iterative_dfs


class TestRecursiveDepthFirstSearch(TestCase):
    """
    Unit Test for recursive Depth First Search implementation
    """
    def test_searching_returns_nodes(self):
        """Test returns expected nodes"""
        graph = {'A': {'B', 'C'},
                 'B': {'A', 'D', 'E'},
                 'C': {'A', 'F'},
                 'D': {'B'},
                 'E': {'B', 'F'},
                 'F': {'C', 'E'}}

        self.assertEqual(recursive_dfs(graph=graph, start='A'), {'A', 'B', 'C', 'D', 'E', 'F'})

    def test_searching_cycle_returns_cycle_nodes(self):
        """Test returns nodes in cycle"""
        graph = {'A': {'B', 'C'},
                 'B': {'D'},
                 'C': {'A', 'F'},
                 'D': {'B'},
                 'E': {'B', 'F'},
                 'F': {'C', 'E'}}

        self.assertEqual(recursive_dfs(graph=graph, start='B'), {'B', 'D'})


class TestIterativeDepthFirstSearch(TestCase):
    """
    Unit Test for iterative Depth First Search implementation
    """
    def test_searching_returns_nodes(self):
        """Test returns expected nodes"""
        graph = {'A': {'B', 'C'},
                 'B': {'A', 'D', 'E'},
                 'C': {'A', 'F'},
                 'D': {'B'},
                 'E': {'B', 'F'},
                 'F': {'C', 'E'}}

        self.assertEqual(iterative_dfs(graph=graph, start='A'), {'A', 'B', 'C', 'D', 'E', 'F'})

    def test_searching_cycle_returns_cycle_nodes(self):
        """Test returns nodes in cycle"""
        graph = {'A': {'B', 'C'},
                 'B': {'D'},
                 'C': {'A', 'F'},
                 'D': {'B'},
                 'E': {'B', 'F'},
                 'F': {'C', 'E'}}

        self.assertEqual(iterative_dfs(graph=graph, start='B'), {'B', 'D'})

