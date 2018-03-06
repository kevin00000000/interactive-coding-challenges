from nose.tools import assert_equal
from nose.tools import assert_true
from enum import Enum  # Python 2 users: Run pip install enum34

class Dependency(object):

    def __init__(self, node_key_before, node_key_after):
        self.node_key_before = node_key_before
        self.node_key_after = node_key_after

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

class BuildOrder(object):

    def __init__(self, dependencies):
        # TODO: Implement me
        self.graph = Graph()
        for dep in dependencies:
            self.graph.add_edge(dep.node_key_before, dep.node_key_after)
        self.order = []
        self.stack = []
        self.marked = {}

    def find_build_order(self):
        # TODO: Implement me
        try:
            for key, node in self.graph.nodes.items():
                if key not in self.marked:
                    self._find_build_order(node)
        except ValueError:
            return None
        return self.order
        
                
    
    def _find_build_order(self, node):
        if node.key in self.stack:
            raise ValueError("Has Cycle")
        self.stack.append(node.key)
        self.marked[node.key] = True
        for key, next_node in node.adj_nodes.items():
            if key not in self.marked:
                self._find_build_order(next_node)
        self.stack.pop()
        self.order.insert(0, node)


class TestBuildOrder(object):

    def __init__(self):
        self.dependencies = [
            Dependency('d', 'g'),
            Dependency('f', 'c'),
            Dependency('f', 'b'),
            Dependency('f', 'a'),
            Dependency('c', 'a'),
            Dependency('b', 'a'),
            Dependency('a', 'e'),
            Dependency('b', 'e'),
        ]

    def test_build_order(self):
        build_order = BuildOrder(self.dependencies)
        processed_nodes = build_order.find_build_order()

        expected_result0 = ('d', 'f')
        expected_result1 = ('c', 'b', 'g')
        assert_true(processed_nodes[0].key in expected_result0)
        assert_true(processed_nodes[1].key in expected_result0)
        assert_true(processed_nodes[2].key in expected_result1)
        assert_true(processed_nodes[3].key in expected_result1)
        assert_true(processed_nodes[4].key in expected_result1)
        assert_true(processed_nodes[5].key is 'a')
        assert_true(processed_nodes[6].key is 'e')

        print('Success: test_build_order')

    def test_build_order_circular(self):
        self.dependencies.append(Dependency('e', 'f'))
        build_order = BuildOrder(self.dependencies)
        processed_nodes = build_order.find_build_order()
        assert_true(processed_nodes is None)

        print('Success: test_build_order_circular')


def main():
    test = TestBuildOrder()
    test.test_build_order()
    test.test_build_order_circular()


if __name__ == '__main__':
    main()