from nose.tools import assert_equal
from nose.tools import raises
import sys

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

class BstValidate_bad(Bst):
    def __init__(self, root):
        super().__init__(root)

    def validate(self):
        if self.root is None:
            return True
        return self._validate(self.root)

    def _validate(self, node):
        bValidLeft = True
        bValidRight = True
        if node.left is not None:
            if self._max(node.left) <= node.data:
                bValidLeft = self._validate(node.left)
            else:
                return False
        if node.right is not None:
            if self._min(node.right) >= node.data:
                bValidRight = self._validate(node.right)
            else:
                return False
        return bValidLeft and bValidRight

    def _min(self, node):
        while node.left is not None:
            node = node.left
        return node.data

    def _max(self, node):
        while node.right is not None:
            node = node.right
        return node.data

class BstValidate(Bst):
    def __init__(self, root):
        super().__init__(root)
    
    def validate(self):
        if self.root is None:
            return True
        return self._validate(self.root, -sys.maxsize, sys.maxsize)

    def _validate(self, node, min, max):
        if node is None:
            return True
        if node.data < min or node.data > max:
            return False
        valid_left = True
        valid_right = True
        if node.left is not None:
            valid_left = self._validate(node.left, min, node.data)
        if node.right is not None:
            valid_right = self._validate(node.right, node.data, max)
        return valid_left and valid_right

class TestBstValidate(object):

    @raises(Exception)
    def test_bst_validate_empty(self):
        validate_bst(None)

    def test_bst_validate(self):
        bst = BstValidate(Node(5))
        bst.insert(8)
        bst.insert(5)
        bst.insert(6)
        bst.insert(4)
        bst.insert(7)
        assert_equal(bst.validate(), True)

        bst = BstValidate(Node(5))
        left = Node(5)
        right = Node(8)
        invalid = Node(20)
        bst.root.left = left
        bst.root.right = right
        bst.root.left.right = invalid
        assert_equal(bst.validate(), False)

        print('Success: test_bst_validate')


def main():
    test = TestBstValidate()
    test.test_bst_validate_empty()
    test.test_bst_validate()


if __name__ == '__main__':
    main()