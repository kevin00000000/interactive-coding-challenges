from nose.tools import assert_equal
import sys


class MagicIndex(object):

    min_index = sys.maxsize

    def find_magic_index(self, array):
        self.min_index = sys.maxsize
        if array is None:
            return -1
        if not array:
            return -1
        self._find_magic_index(array, 0, len(array)-1)
        if self.min_index == sys.maxsize:
            return -1
        return self.min_index
    
    def _find_magic_index(self, array, start, end):
        if start > end:
            return
        mid = (start + end) // 2
        if array[mid] == mid:
            if mid < self.min_index:
                self.min_index = mid
            self._find_magic_index(array, start, min(mid-1, array[mid]))
        else:
            self._find_magic_index(array, start, min(mid-1, array[mid]))
            if self.min_index > min(mid-1, array[mid]):
                self._find_magic_index(array, max(mid+1, array[mid]), end)

        


class TestFindMagicIndex(object):

    def test_find_magic_index(self):
        magic_index = MagicIndex()
        assert_equal(magic_index.find_magic_index(None), -1)
        assert_equal(magic_index.find_magic_index([]), -1)
        array = [-4, -2, 2, 6, 6, 6, 6, 10]
        assert_equal(magic_index.find_magic_index(array), 2)
        array = [-4, -2, 1, 6, 6, 6, 6, 10]
        assert_equal(magic_index.find_magic_index(array), 6)
        array = [-4, -2, 1, 6, 6, 6, 7, 10]
        assert_equal(magic_index.find_magic_index(array), -1)
        print('Success: test_find_magic')


def main():
    test = TestFindMagicIndex()
    test.test_find_magic_index()


if __name__ == '__main__':
    main()