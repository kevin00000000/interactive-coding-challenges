from nose.tools import assert_equal
from enum import Enum

class State(Enum):

    unvisited = 0
    visiting = 1
    visited = 2


class Node:

    def __init__(self, key):
        self.key = key
        self.visit_state = State.unvisited
        self.incoming_edges = 0
        self.adj_nodes = {}  # Key = key, val = Node
        self.adj_weights = {}  # Key = key, val = weight

    def __repr__(self):
        return str(self.key)

    def __lt__(self, other):
        return self.key < other.key

    def add_neighbor(self, neighbor, weight=0):
        # TODO: Implement me
        if neighbor is None or weight is None:
            raise TypeError("Invalid neighbor")
        if neighbor.key not in self.adj_nodes:
            neighbor.incoming_edges += 1
        self.adj_nodes[neighbor.key] = neighbor
        self.adj_weights[neighbor.key] = weight

    def remove_neighbor(self, neighbor):
        # TODO: Implement me
        if neighbor is None:
            raise TypeError("Invalid neighbor")
        if neighbor.key not in self.adj_nodes:
            return
        neighbor.incoming_edges -= 1
        del self.adj_nodes[neighbor.key]
        del self.adj_weights[neighbor.key]


class Graph:

    def __init__(self):
        self.nodes = {}  # Key = key, val = Node

    def add_node(self, id):
        # TODO: Implement me
        if id in self.nodes:
            return
        self.nodes[id] = Node(id)
        return self.nodes[id]

    def add_edge(self, source, dest, weight=0):
        # TODO: Implement me
        if source is None or dest is None:
            raise TypeError("Invalid key")
        if source not in self.nodes:
            self.nodes[source] = Node(source)
        if dest not in self.nodes:
            self.nodes[dest] = Node(dest)
        if(dest not in self.nodes[source].adj_nodes):
            self.nodes[dest].incoming_edges += 1
        self.nodes[source].adj_nodes[dest] = self.nodes[dest]
        self.nodes[source].adj_weights[dest] = weight

    def add_undirected_edge(self, source, dest, weight=0):
        # TODO: Implement me
        self.add_edge(source, dest, weight)
        self.add_edge(dest, source, weight)

class GraphDfs(Graph):
    def __init__(self):
        super().__init__()
        self.marked = {}#Key:key,Val:bool
    def dfs(self, root, visit_func):
        visit_func(root)
        self.marked[root.key] = True
        for key, node in root.adj_nodes.items():
            if key not in self.marked:
                self.dfs(node, visit_func)

class Results(object):

    def __init__(self):
        self.results = []

    def add_result(self, result):
        # TODO: Clean this up
        # Simplifies challenge coding and unit testing
        # but makes this function look less appealing
        self.results.append(int(str(result)))

    def clear_results(self):
        self.results = []

    def __str__(self):
        return str(self.results)

class TestDfs(object):

    def __init__(self):
        self.results = Results()

    def test_dfs(self):
        nodes = []
        graph = GraphDfs()
        for id in range(0, 6):
            nodes.append(graph.add_node(id))
        graph.add_edge(0, 1, 5)
        graph.add_edge(0, 4, 3)
        graph.add_edge(0, 5, 2)
        graph.add_edge(1, 3, 5)
        graph.add_edge(1, 4, 4)
        graph.add_edge(2, 1, 6)
        graph.add_edge(3, 2, 7)
        graph.add_edge(3, 4, 8)
        graph.dfs(nodes[0], self.results.add_result)
        assert_equal(str(self.results), "[0, 1, 3, 2, 4, 5]")

        print('Success: test_dfs')


def main():
    test = TestDfs()
    test.test_dfs()


if __name__ == '__main__':
    main()