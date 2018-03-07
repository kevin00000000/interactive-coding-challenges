from nose.tools import assert_equal
from collections import deque
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

class GraphShortestPath(Graph):
    def __init__(self):
        super().__init__()
        self.marked = {}
        self.pre_node = {}

    def shortest_path(self, source_key, dest_key):
        if source_key is None or dest_key is None:
            return None
        if source_key not in self.nodes.keys() or dest_key not in self.nodes.keys():
            return None
        if source_key == dest_key:
            return [source_key]
        self.pre_node[source_key] = None
        self.bfs(self.nodes[source_key])
        if dest_key not in self.marked:
            return None
        result = []
        while self.pre_node[dest_key] is not None:
            result.insert(0, dest_key)
            dest_key = self.pre_node[dest_key]
        result.insert(0, source_key)
        return result

    def bfs(self, node):
        self.marked.clear()
        queue = deque()
        queue.append(node)
        self.marked[node.key] = True
        while len(queue) != 0:
            node = queue.popleft()
            for next_node in node.adj_nodes.values():
                if next_node.key not in self.marked:
                    self.marked[next_node.key]= True
                    self.pre_node[next_node.key] = node.key
                    queue.append(next_node)
                
                



class TestShortestPath(object):

    def test_shortest_path(self):
        nodes = []
        graph = GraphShortestPath()
        for id in range(0, 6):
            nodes.append(graph.add_node(id))
        graph.add_edge(0, 1)
        graph.add_edge(0, 4)
        graph.add_edge(0, 5)
        graph.add_edge(1, 3)
        graph.add_edge(1, 4)
        graph.add_edge(2, 1)
        graph.add_edge(3, 2)
        graph.add_edge(3, 4)

        assert_equal(graph.shortest_path(nodes[0].key, nodes[2].key), [0, 1, 3, 2])
        assert_equal(graph.shortest_path(nodes[0].key, nodes[0].key), [0])
        assert_equal(graph.shortest_path(nodes[4].key, nodes[5].key), None)

        print('Success: test_shortest_path')


def main():
    test = TestShortestPath()
    test.test_shortest_path()


if __name__ == '__main__':
    main()