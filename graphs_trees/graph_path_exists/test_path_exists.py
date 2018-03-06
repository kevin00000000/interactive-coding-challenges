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
        if neighbor is None or weight is None:
            raise TypeError('neighbor or weight cannot be None')
        neighbor.incoming_edges += 1
        self.adj_weights[neighbor.key] = weight
        self.adj_nodes[neighbor.key] = neighbor

    def remove_neighbor(self, neighbor):
        if neighbor is None:
            raise TypeError('neighbor cannot be None')
        if neighbor.key not in self.adj_nodes:
            raise KeyError('neighbor not found')
        neighbor.incoming_edges -= 1
        del self.adj_weights[neighbor.key]
        del self.adj_nodes[neighbor.key]


class Graph:

    def __init__(self):
        self.nodes = {}  # Key = key, val = Node

    def add_node(self, key):
        if key is None:
            raise TypeError('key cannot be None')
        if key not in self.nodes:
            self.nodes[key] = Node(key)
        return self.nodes[key]

    def add_edge(self, source_key, dest_key, weight=0):
        if source_key is None or dest_key is None:
            raise KeyError('Invalid key')
        if source_key not in self.nodes:
            self.add_node(source_key)
        if dest_key not in self.nodes:
            self.add_node(dest_key)
        self.nodes[source_key].add_neighbor(self.nodes[dest_key], weight)

    def add_undirected_edge(self, src_key, dst_key, weight=0):
        if src_key is None or dst_key is None:
            raise TypeError('key cannot be None')
        self.add_edge(src_key, dst_key, weight)
        self.add_edge(dst_key, src_key, weight)

class GraphPathExists(Graph):
    def __init__(self):
        super().__init__()
        self.marked = {}

    def path_exists(self, start, end):
        self.marked.clear()
        self.dfs(start)
        return end in self.marked
    
    def dfs(self, s):
        if s not in self.marked:
            self.marked[s] = True
            for node in s.adj_nodes.values():
                self.dfs(node)
        

class TestPathExists(object):

    def test_path_exists(self):
        nodes = []
        graph = GraphPathExists()
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

        assert_equal(graph.path_exists(nodes[0], nodes[2]), True)
        assert_equal(graph.path_exists(nodes[0], nodes[0]), True)
        assert_equal(graph.path_exists(nodes[4], nodes[5]), False)

        print('Success: test_path_exists')


def main():
    test = TestPathExists()
    test.test_path_exists()


if __name__ == '__main__':
    main()