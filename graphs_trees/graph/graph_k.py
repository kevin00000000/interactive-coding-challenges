from enum import Enum  # Python 2 users: Run pip install enum34


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