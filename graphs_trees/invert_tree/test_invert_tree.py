from nose.tools import assert_equal, assert_raises

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

class InverseBst(Bst):
    def __init__(self, root):
        super().__init__(root)
    
    def invert_tree(self):
        if self.root is None:
            raise TypeError("Can't invert empty tree")
        return self._invert_tree(self.root)

    def _invert_tree(self, node):
        if node is None:
            return None
        node.left = self._invert_tree(node.left)
        node.right = self._invert_tree(node.right)
        node.left, node.right = node.right, node.left
        return node 

class TestInvertTree(object):

    def test_invert_tree(self):
        root = Node(5)
        bst = InverseBst(root)
        node2 = bst.insert(2)
        node3 = bst.insert(3)
        node1 = bst.insert(1)
        node7 = bst.insert(7)
        node6 = bst.insert(6)
        node9 = bst.insert(9)
        result = bst.invert_tree()
        assert_equal(result, root)
        assert_equal(result.left, node7)
        assert_equal(result.right, node2)
        assert_equal(result.left.left, node9)
        assert_equal(result.left.right, node6)
        assert_equal(result.right.left, node3)
        assert_equal(result.right.right, node1)
        print('Success: test_invert_tree')


def main():
    test = TestInvertTree()
    test.test_invert_tree()


if __name__ == '__main__':
    main()