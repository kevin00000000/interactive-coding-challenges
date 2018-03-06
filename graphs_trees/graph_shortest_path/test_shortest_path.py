from nose.tools import assert_equal
from enum import Enum
import sys


class PriorityQueueNode(object):

    def __init__(self, obj, key):
        self.obj = obj
        self.key = key

    def __repr__(self):
        return str(self.obj) + ': ' + str(self.key)


class PriorityQueue(object):

    def __init__(self):
        self.queue = []

    def insert(self, node):
        if node is not None:
            self.queue.append(node)
            return self.queue[-1]
        return None

    def extract_min(self):
        if not self.queue:
            return None
        minimum = sys.maxsize
        for index, node in enumerate(self.queue):
            if node.key < minimum:
                minimum = node.key
                minimum_index = index
        node = self.queue.pop(minimum_index)
        return node.obj

    def decrease_key(self, obj, new_key):
        for node in self.queue:
            if node.obj is obj:
                node.key = new_key
                return node
        return None

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

class ShortestPath(object):

    def __init__(self, graph):
        # TODO: Implement me
        self.graph = graph
        self.path_weight = {}
        self.path_weight = {}
        self.marked = {}
        self.result = []
        self.last_node_key = {}
        self.priority_queue = PriorityQueue()

    def find_shortest_path(self, start_node_key, end_node_key):
        # TODO: Implement me
        if start_node_key not in self.graph.nodes.keys() or end_node_key not in self.graph.nodes.keys():
            raise TypeError("Invalide node")
        self.path_weight[start_node_key] = 0
        self.priority_queue.insert(PriorityQueueNode(start_node_key, 0))
        while len(self.priority_queue.queue) != 0:
            key = self.priority_queue.extract_min()
            if key not in self.marked:
                self.marked[key] = True
                self.relax(key)
        while end_node_key != start_node_key:
            self.result.insert(0, end_node_key)
            end_node_key = self.last_node_key[end_node_key]
        self.result.insert(0, start_node_key)
        return self.result

    def relax(self, node_key):
        for key in self.graph.nodes[node_key].adj_nodes.keys():
            if key not in self.path_weight or self.path_weight[key] > self.path_weight[node_key] + self.graph.nodes[node_key].adj_weights[key]:
                self.path_weight[key] = self.path_weight[node_key] + self.graph.nodes[node_key].adj_weights[key]
                self.priority_queue.insert(PriorityQueueNode(key, self.path_weight[key]))
                self.last_node_key[key] = node_key


class TestShortestPath(object):

    def test_shortest_path(self):
        graph = Graph()
        graph.add_edge('a', 'b', weight=5)
        graph.add_edge('a', 'c', weight=3)
        graph.add_edge('a', 'e', weight=2)
        graph.add_edge('b', 'd', weight=2)
        graph.add_edge('c', 'b', weight=1)
        graph.add_edge('c', 'd', weight=1)
        graph.add_edge('d', 'a', weight=1)
        graph.add_edge('d', 'g', weight=2)
        graph.add_edge('d', 'h', weight=1)
        graph.add_edge('e', 'a', weight=1)
        graph.add_edge('e', 'h', weight=4)
        graph.add_edge('e', 'i', weight=7)
        graph.add_edge('f', 'b', weight=3)
        graph.add_edge('f', 'g', weight=1)
        graph.add_edge('g', 'c', weight=3)
        graph.add_edge('g', 'i', weight=2)
        graph.add_edge('h', 'c', weight=2)
        graph.add_edge('h', 'f', weight=2)
        graph.add_edge('h', 'g', weight=2)
        shortest_path = ShortestPath(graph)
        result = shortest_path.find_shortest_path('a', 'i')
        assert_equal(result, ['a', 'c', 'd', 'g', 'i'])
        assert_equal(shortest_path.path_weight['i'], 8)

        print('Success: test_shortest_path')


def main():
    test = TestShortestPath()
    test.test_shortest_path()


if __name__ == '__main__':
    main()