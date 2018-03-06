from nose.tools import assert_equal
from nose.tools import raises

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

class BstBalance(Bst):
    def __init__(self, root):
        super().__init__(root)
    
    def check_balance(self):
        if self.root is None:
            raise TypeError("Can't check empty tree")
        height = self._check_balance(self.root)
        return height != -1

    def _check_balance(self, node):
        if node is None:
            return 0
        height_left = self._check_balance(node.left)
        if height_left == -1:
            return -1
        height_right = self._check_balance(node.right)
        if height_right == -1:
            return -1
        diff = abs(height_right-height_left)
        if diff > 1:
            return -1
        height = 1 + max(height_left, height_right)
        return height

class TestCheckBalance(object):

    @raises(TypeError)
    def test_check_balance_empty(self):
        bst = BstBalance(None)
        bst.check_balance()

    def test_check_balance(self):
        bst = BstBalance(Node(5))
        assert_equal(bst.check_balance(), True)

        bst.insert(3)
        bst.insert(8)
        bst.insert(1)
        bst.insert(4)
        assert_equal(bst.check_balance(), True)

        bst = BstBalance(Node(5))
        bst.insert(3)
        bst.insert(8)
        bst.insert(9)
        bst.insert(10)
        assert_equal(bst.check_balance(), False)

        bst = BstBalance(Node(3))
        bst.insert(2)
        bst.insert(1)
        bst.insert(5)
        bst.insert(4)
        bst.insert(6)
        bst.insert(7)
        assert_equal(bst.check_balance(), True)

        print('Success: test_check_balance')


def main():
    test = TestCheckBalance()
    test.test_check_balance_empty()
    test.test_check_balance()


if __name__ == '__main__':
    main()