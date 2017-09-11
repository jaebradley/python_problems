def recursive_dfs(graph, start, visited=None):
    """
    Returns a set of visited nodes given a graph that represents a mapping of a node to its children
    and some start point.

    Is implemented using recursion.

    :param graph: A dictionary / map of nodes to their children
    :param start: A starting node
    :param visited: An optional set of previously visited nodes
    :return: A set of all visited nodes
    """
    if visited is None:
        visited = set()

    visited.add(start)

    for child in graph[start] - visited:
        if child not in visited:
            recursive_dfs(graph, child, visited)

    return visited


def iterative_dfs(graph, start):
    """
    Returns a set of visited nodes given a graph that represents a mapping of a node to its children
    and some start point.

    Is implemented by using a stack to keep track of which nodes still need to be evaluated.

    :param graph: A dictionary / map of nodes to their children
    :param start: A starting node
    :return:
    """
    visited = set()
    nodes = [start]

    while len(nodes) > 0:
        node = nodes.pop()
        if node not in visited:
            visited.add(node)
            nodes.extend(graph[node] - visited)

    return visited
