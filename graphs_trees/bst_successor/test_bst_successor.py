from nose.tools import assert_equal
from nose.tools import raises

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

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
        self._root = self._insert(node, self._root, None)
        return node
    
    def _insert(self, node, child, parent):
        if child is None:
            child = node
            child.parent = parent
        elif child.data > node.data:
            child.left = self._insert(node, child.left, child)
        else:
            child.right = self._insert(node, child.right, child)
        return child

class BstSuccessor():
    def get_next(self, node):
        if node is None:
            raise TypeError
        if node.right is not None:
            node = node.right
            while node.left is not None:
                node = node.left
            return node.data
        else:
            parent = node.parent
            while parent is not None and parent.left != node:
                node = parent
                parent = parent.parent
            if parent is not None:
                return parent.data
            else:
                return None


class TestBstSuccessor(object):

    @raises(Exception)
    def test_bst_successor_empty(self):
        bst_successor = BstSuccessor()
        bst_successor.get_next(None)

    def test_bst_successor(self):
        nodes = {}
        node = Node(5)
        nodes[5] = node
        bst = Bst(nodes[5])
        nodes[3] = bst.insert(3)
        nodes[8] = bst.insert(8)
        nodes[2] = bst.insert(2)
        nodes[4] = bst.insert(4)
        nodes[6] = bst.insert(6)
        nodes[12] = bst.insert(12)
        nodes[1] = bst.insert(1)
        nodes[7] = bst.insert(7)
        nodes[10] = bst.insert(10)
        nodes[15] = bst.insert(15)
        nodes[9] = bst.insert(9)

        bst_successor = BstSuccessor()
        assert_equal(bst_successor.get_next(nodes[4]), 5)
        assert_equal(bst_successor.get_next(nodes[5]), 6)
        assert_equal(bst_successor.get_next(nodes[8]), 9)
        assert_equal(bst_successor.get_next(nodes[15]), None)

        print('Success: test_bst_successor')


def main():
    test = TestBstSuccessor()
    test.test_bst_successor()
    test.test_bst_successor_empty()


if __name__ == '__main__':
    main()