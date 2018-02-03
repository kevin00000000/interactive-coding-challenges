from nose.tools import assert_equal, assert_raises

class Array(object):
    
    def search_sorted_array(self, array, val):
        if array is None or val is None:
            raise TypeError('array or val cannot be None')
        if not array:
            return None
        return self._search_sorted_array(array, val, start=0, end=len(array)-1)

    def _search_sorted_array(self, array, val, start, end):
        if end < start:
            return None
        mid = (start + end) // 2
        if array[mid] == val:
            return mid
        if array[start] < array[mid]:
            if array[start]<=val<array[mid]:
                return self._search_sorted_array(array, val, start, mid-1)
            else:
                return self._search_sorted_array(array, val, mid+1, end)
        elif array[end] > array[mid]:
            if array[mid] < val <=array[end]:
                return self._search_sorted_array(array, val, mid+1, end)
            else:
                return self._search_sorted_array(array, val, start, mid-1)
        else:
            if array[mid] == array[end] and array[mid] == array[start]:
                result = self._search_sorted_array(array, val, start, mid-1)
                if not result:
                    return self._search_sorted_array(array, val, mid+1, end)
                else:
                    return result
            elif array[mid] == array[end]:
                return self._search_sorted_array(array, val, start, mid-1)
            else:
                return self._search_sorted_array(array, val, mid+1, end)
                
class TestArray(object):

    def test_search_sorted_array(self):
        array = Array()
        assert_raises(TypeError, array.search_sorted_array, None)
        assert_equal(array.search_sorted_array([3, 1, 2], 0), None)
        assert_equal(array.search_sorted_array([3, 1, 2], 0), None)
        data = [10, 12, 14,  1,  3,  5,  6,  7,  8,  9]
        assert_equal(array.search_sorted_array(data, val=1), 3)
        data = [ 1,  1,  2,  1,  1,  1,  1,  1,  1,  1]
        assert_equal(array.search_sorted_array(data, val=2), 2)
        print('Success: test_search_sorted_array')


def main():
    test = TestArray()
    test.test_search_sorted_array()


if __name__ == '__main__':
    main()