class Node:
    def __init__(self, value, children):
        self.value = value
        self.children = children


def depth_first_search(root, target, visited=None, nodes=None):
    if visited is None:
        visited = set()

    if nodes is None:
        nodes = []

    if root.value == target:
        return True

    visited.add(root.value)
    nodes.append(root.value)

    for child in root.children:
        if child.value not in visited:
            if depth_first_search(child, target, visited, nodes):
                return True

    nodes.pop()

    return False

