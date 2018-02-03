from nose.tools import assert_equal, assert_raises

class QuickSort(object):
    def sort(self, data):
        self._sort(data, 0, len(data))
        return data

    def _sort(self, data, low, high):
        if data is None:
            raise TypeError
        if high-low < 2:
            return
        mid_index = self._mid2(data, low, high)
        self._sort(data, low, mid_index)
        self._sort(data, mid_index+1, high)
        return

    def _mid(self, data, low, high):
        i = low + 1
        standard = data[low]
        more_index = None
        while i < high:
            if data[i] < standard:
                if more_index is not None:
                    data[i], data[more_index] = data[more_index], data[i]
                    more_index += 1
            else:
                if more_index is None:
                    more_index = i
            i += 1
        if more_index is None:
            data[low], data[high-1] = data[high-1], data[low]
            return high-1
        else:
            data[low], data[more_index-1] = data[more_index-1], data[low]
        return more_index-1

    def _mid2(self, data, low, high):
        i = low + 1
        j = high
        standard = data[low]
        while i < j:
            while i < j:
                if data[i] > standard:
                    break
                i += 1
            if i < j:
                while i < j:
                    if data[j-1] < standard:
                        data[i], data[j-1] = data[j-1], data[i]
                        break
                    j -= 1
                if i < j:
                    j -= 1
                    i += 1
                    continue     
        data[low], data[j-1] = data[j-1], data[low]
        return j-1


class TestQuickSort(object):

    def test_quick_sort(self):
        quick_sort = QuickSort()

        print('None input')
        assert_raises(TypeError, quick_sort.sort, None)

        print('Empty input')
        assert_equal(quick_sort.sort([]), [])

        print('One element')
        assert_equal(quick_sort.sort([5]), [5])

        print('Two or more elements')
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        assert_equal(quick_sort.sort(data), sorted(data))

        print('Success: test_quick_sort\n')


def main():
    test = TestQuickSort()
    test.test_quick_sort()


if __name__ == '__main__':
    main()