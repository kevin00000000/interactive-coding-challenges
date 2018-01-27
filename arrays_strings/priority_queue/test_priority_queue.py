from nose.tools import assert_equal
import sys
#from priority_queue import PriorityQueue, PriorityQueueNode


class PriorityQueueNode(object):

    def __init__(self, obj, key):
        self.obj = obj
        self.key = key
    
    def __repr__(self):
        return str(self.obj)+":"+str(self.key)

class PriorityQueue_sort_when_change(object):
    def __init__(self):
        self.array = []
    
    def __len__(self):
        return len(self.array)

    def insert(self, node):
        self.array.append(node)
        self.array.sort(key=lambda node: node.key, reverse=True)
        return node

    def extract_min(self):
        if self.array:
            return self.array.pop()
        return None

    def decrease_key(self, obj, new_key):
        for node in self.array:
            if node.obj == obj:
                break
        else:
            return
        node.key = new_key
        self.array.sort(key=lambda node: node.key, reverse=True)
        return node

class PriorityQueue_sort_when_extract(object):
    def __init__(self):
        self.array = []
    
    def __len__(self):
        return len(self.array)

    def insert(self, node):
        self.array.append(node)
        return node

    def extract_min(self):
        if not self.array:
            return None
        self.array.sort(key=lambda node: node.key, reverse=True)
        node = self.array.pop()
        return node

    def decrease_key(self, obj, new_key):
        for node in self.array:
            if node.obj == obj:
                node.key = new_key
                return node
        else:
            return None
        

class PriorityQueue(object):
    def __init__(self):
        self.array = []
    
    def __len__(self):
        return len(self.array)

    def insert(self, node):
        self.array.append(node)
        return node

    def extract_min(self):
        if not self.array:
            return None
        minimum = sys.maxsize
        min_index = 0
        for index, node in enumerate(self.array):
            if node.key < minimum:
                minimum = node.key
                min_index = index
        return self.array.pop(min_index)


    def decrease_key(self, obj, new_key):
        for node in self.array:
            if node.obj == obj:
                node.key = new_key
                return node
        else:
            return None

class TestPriorityQueue(object):

    def test_priority_queue(self):
        priority_queue = PriorityQueue()
        assert_equal(priority_queue.extract_min(), None)
        priority_queue.insert(PriorityQueueNode('a', 20))
        priority_queue.insert(PriorityQueueNode('b', 5))
        priority_queue.insert(PriorityQueueNode('c', 15))
        priority_queue.insert(PriorityQueueNode('d', 22))
        priority_queue.insert(PriorityQueueNode('e', 40))
        priority_queue.insert(PriorityQueueNode('f', 3))
        priority_queue.decrease_key('f', 2)
        priority_queue.decrease_key('a', 19)
        mins = []
        while priority_queue.array:
            mins.append(priority_queue.extract_min().key)
        assert_equal(mins, [2, 5, 15, 19, 22, 40])
        print('Success: test_min_heap')


def main():
    test = TestPriorityQueue()
    test.test_priority_queue()


if __name__ == '__main__':
    main()