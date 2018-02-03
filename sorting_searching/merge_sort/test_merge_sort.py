from nose.tools import assert_equal, assert_raises

class MergeSort(object):
    def sort(self, data):
        if data is None:
            raise TypeError
        if len(data) < 2:
            return data
        left = self.sort(data[0:len(data)//2])
        right = self.sort(data[len(data)//2:])
        data = self._merge(left, right)
        return data
    
    def _merge(self, left, right):
        result = []
        i = 0
        j = 0
        while i<len(left) or j<len(right):
            if i==len(left):
                result.extend(right[j:])
                return result
            if j==len(right):
                result.extend(left[i:])
                return result
            if left[i]<right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        return result


class TestMergeSort(object):

    def test_merge_sort(self):
        merge_sort = MergeSort()

        print('None input')
        assert_raises(TypeError, merge_sort.sort, None)

        print('Empty input')
        assert_equal(merge_sort.sort([]), [])

        print('One element')
        assert_equal(merge_sort.sort([5]), [5])

        print('Two or more elements')
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        assert_equal(merge_sort.sort(data), sorted(data))

        print('Success: test_merge_sort')


def main():
    test = TestMergeSort()
    test.test_merge_sort()


if __name__ == '__main__':
    main()