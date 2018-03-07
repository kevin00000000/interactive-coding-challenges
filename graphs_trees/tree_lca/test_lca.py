from nose.tools import assert_equal

class Node(object):

    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.key)

class BinaryTree(object):

    def lca(self, root, node1, node2):
        # TODO: Implement me
        if not self._node_in_root(root, node1) or not self._node_in_root(root, node2):
            return None
        if root==node1 or root==node2:
            return root
        node1_in_left = self._node_in_root(root.left, node1)
        node1_in_right = self._node_in_root(root.right, node1)
        node2_in_left = self._node_in_root(root.left, node2)
        node2_in_right = self._node_in_root(root.right, node2)
        if node1_in_left and node2_in_left:
            return self.lca(root.left, node1, node2)
        elif node1_in_right and node2_in_right:
            return self.lca(root.right, node1, node2)
        else:
            return root
    
    def _node_in_root(self, root, node):
        if root is None:
            return False
        result = []
        self._dfs(root, result)
        return node.key in result
    
    def _dfs(self, root, result):
        if root is None:
            return
        result.append(root.key)
        self._dfs(root.left, result)
        self._dfs(root.right, result)



class TestLowestCommonAncestor(object):

    def test_lca(self):
        node10 = Node(10)
        node5 = Node(5)
        node12 = Node(12)
        node3 = Node(3)
        node1 = Node(1)
        node8 = Node(8)
        node9 = Node(9)
        node18 = Node(18)
        node20 = Node(20)
        node40 = Node(40)
        node3.left = node1
        node3.right = node8
        node5.left = node12
        node5.right = node3
        node20.left = node40
        node9.left = node18
        node9.right = node20
        node10.left = node5
        node10.right = node9
        root = node10
        node0 = Node(0)
        binary_tree = BinaryTree()
        assert_equal(binary_tree.lca(root, node0, node5), None)
        assert_equal(binary_tree.lca(root, node5, node0), None)
        assert_equal(binary_tree.lca(root, node1, node8), node3)
        assert_equal(binary_tree.lca(root, node12, node8), node5)
        assert_equal(binary_tree.lca(root, node12, node40), node10)
        assert_equal(binary_tree.lca(root, node9, node20), node9)
        assert_equal(binary_tree.lca(root, node3, node5), node5)
        print('Success: test_lca')


def main():
    test = TestLowestCommonAncestor()
    test.test_lca()


if __name__ == '__main__':
    main()