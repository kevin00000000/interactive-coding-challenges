from nose.tools import assert_equal
import sys

class MinHeap(object):

    def __init__(self):
        # TODO: Implement me
        self.data = [None]
        self.length = 0
    
    def __len__(self):
        return self.length

    @property
    def array(self):
        return self.data[1:len(self.data)]
        

    def extract_min(self):
        # TODO: Implement me
        if self.length == 0:
            return None
        result = self.data[1]
        self.data[1], self.data[self.length] = self.data[self.length], self.data[1]
        self.length -= 1
        self._swim_down(1)
        return result   

    def peek_min(self):
        # TODO: Implement me
        if self.length == 0:
            return None
        result = self.data[1]
        return result

    def insert(self, data):
        # TODO: Implement me
        self.data.append(data)
        self.length += 1
        self._bubble_up(self.length)

    def _bubble_up(self, index):
        # TODO: Implement me
        if index//2 > 0 and self.data[index] < self.data[index//2]:
            self.data[index], self.data[index//2] = self.data[index//2], self.data[index]
            self._bubble_up(index//2)
    
    def _swim_down(self, index):
        if self.length == 0:
            return
        if index*2 <= self.length:
            left = self.data[index*2]
            right = sys.maxsize if index*2+1>self.length else self.data[index*2+1]
            if left<right:
                self.data[index], self.data[index*2] = self.data[index*2], self.data[index]
                self._swim_down(index*2)
            else:
                self.data[index], self.data[index*2+1] = self.data[index*2+1], self.data[index]
                self._swim_down(index*2+1)


class TestMinHeap(object):

    def test_min_heap(self):
        heap = MinHeap()
        assert_equal(heap.peek_min(), None)
        assert_equal(heap.extract_min(), None)
        heap.insert(20)
        assert_equal(heap.array[0], 20)
        heap.insert(5)
        assert_equal(heap.array[0], 5)
        assert_equal(heap.array[1], 20)
        heap.insert(15)
        assert_equal(heap.array[0], 5)
        assert_equal(heap.array[1], 20)
        assert_equal(heap.array[2], 15)
        heap.insert(22)
        assert_equal(heap.array[0], 5)
        assert_equal(heap.array[1], 20)
        assert_equal(heap.array[2], 15)
        assert_equal(heap.array[3], 22)
        heap.insert(40)
        assert_equal(heap.array[0], 5)
        assert_equal(heap.array[1], 20)
        assert_equal(heap.array[2], 15)
        assert_equal(heap.array[3], 22)
        assert_equal(heap.array[4], 40)
        heap.insert(3)
        assert_equal(heap.array[0], 3)
        assert_equal(heap.array[1], 20)
        assert_equal(heap.array[2], 5)
        assert_equal(heap.array[3], 22)
        assert_equal(heap.array[4], 40)
        assert_equal(heap.array[5], 15)
        mins = []
        while heap:
            mins.append(heap.extract_min())
        assert_equal(mins, [3, 5, 15, 20, 22, 40])
        print('Success: test_min_heap')

        
def main():
    test = TestMinHeap()
    test.test_min_heap()

    
if __name__ == '__main__':
    main()