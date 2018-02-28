class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Bst(object):
    def __init__(self, root=None):
        self._root = root

    @property
    def root(self):
        return self._root

    def insert(self, data):
        if data is None:
            raise TypeError
        node = Node(data)
        self._root = self._insert(node, self._root)
        return node
    
    def _insert(self, node, root):
        if root is None:
            root = node
        elif root.data > node.data:
            root.left = self._insert(node, root.left)
        else:
            root.right = self._insert(node, root.right)
        return root

