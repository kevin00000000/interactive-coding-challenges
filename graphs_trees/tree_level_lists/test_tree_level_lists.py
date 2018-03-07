from nose.tools import assert_equal
from collections import OrderedDict

class Node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return str(self.data)


class Bst(object):

    def __init__(self, root=None):
        self.root = root

    def insert(self, data):
        if data is None:
            raise TypeError('data cannot be None')
        if self.root is None:
            self.root = Node(data)
            return self.root
        else:
            return self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            return Node(data)
        if data <= node.data:
            if node.left is None:
                node.left = self._insert(node.left, data)
                node.left.parent = node
                return node.left
            else:
                return self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = self._insert(node.right, data)
                node.right.parent = node
                return node.right
            else:
                return self._insert(node.right, data)

class BstLevelLists(Bst):

    def create_level_lists(self):
        # TODO: Implement me
        self.level_lists = OrderedDict()
        self._height(self.root, 0)
        result = []
        for value in self.level_lists.values():
            result.append(value)
        return result
    
    def _height(self, node, n):
        if node is None:
            return
        if n not in self.level_lists:
            self.level_lists[n] = []
        self.level_lists[n].append(node)
        self._height(node.left, n+1)
        self._height(node.right, n+1)

class Results(object):

    def __init__(self):
        self.results = []

    def add_result(self, result):
        # TODO: Clean this up
        # Simplifies challenge coding and unit testing
        # but makes this function look less appealing
        self.results.append(int(str(result)))

    def clear_results(self):
        self.results = []

    def __str__(self):
        return str(self.results)

class TestTreeLevelLists(object):

    def test_tree_level_lists(self):
        bst = BstLevelLists(Node(5))
        bst.insert(3)
        bst.insert(8)
        bst.insert(2)
        bst.insert(4)
        bst.insert(1)
        bst.insert(7)
        bst.insert(6)
        bst.insert(9)
        bst.insert(10)
        bst.insert(11)

        levels = bst.create_level_lists()
        results_list = []
        for level in levels:
            results = Results()
            for node in level:
                results.add_result(node)
            results_list.append(results)

        assert_equal(str(results_list[0]), '[5]')
        assert_equal(str(results_list[1]), '[3, 8]')
        assert_equal(str(results_list[2]), '[2, 4, 7, 9]')
        assert_equal(str(results_list[3]), '[1, 6, 10]')
        assert_equal(str(results_list[4]), '[11]')

        print('Success: test_tree_level_lists')


def main():
    test = TestTreeLevelLists()
    test.test_tree_level_lists()


if __name__ == '__main__':
    main()