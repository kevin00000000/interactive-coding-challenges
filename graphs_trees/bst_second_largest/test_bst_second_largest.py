from nose.tools import assert_equal, assert_raises

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

class Solution(Bst):
    def __init__(self, root):
        super().__init__(root)
    def find_second_largest(self):
        if self.root is None:
            raise TypeError
        if self.root.left is None and self.root.right is None:
            raise ValueError
        target = None
        if self.root.right is not None:
            node = self.root
            while node.right is not None:
                node = node.right
            target = node.parent
        else:
            node = self.root.left
            while node.right is not None:
                node = node.right
            target = node
        return target

class TestBstSecondLargest(object):

    def test_bst_second_largest(self):
        bst = Solution(None)
        assert_raises(TypeError, bst.find_second_largest)
        root = Node(10)
        bst = Solution(root)
        node5 = bst.insert(5)
        node15 = bst.insert(15)
        node3 = bst.insert(3)
        node8 = bst.insert(8)
        node12 = bst.insert(12)
        node20 = bst.insert(20)
        node2 = bst.insert(2)
        node4 = bst.insert(4)
        node30 = bst.insert(30)
        assert_equal(bst.find_second_largest(), node20)
        root = Node(10)
        bst = Solution(root)
        node5 = bst.insert(5)
        node3 = bst.insert(3)
        node7 = bst.insert(7)
        assert_equal(bst.find_second_largest(), node7)
        print('Success: test_bst_second_largest')


def main():
    test = TestBstSecondLargest()
    test.test_bst_second_largest()


if __name__ == '__main__':
    main()