from nose.tools import assert_equal, assert_raises
import sys

class SelectionSort(object):
    def sort(self, data):
        if data is None:
            raise TypeError
        if len(data) < 2:
            return data
        min_value = sys.maxsize
        temp = 0
        for i, value_i in enumerate(data):
            temp = i
            min_value = value_i
            for j, value_j in enumerate(data[i:]):
                if value_j < min_value:
                    temp = j+i
                    min_value = value_j
            data[i], data[temp] = data[temp], data[i]
        return data

    def sort_recursive(self, data):
        if data is None:
            raise TypeError
        if len(data) < 2:
            return data
        min_value = sys.maxsize
        temp = 0
        for i, value_i in enumerate(data):
            if value_i < min_value:
                temp = i
                min_value = value_i
        data[0], data[temp] = data[temp], data[0]
        result = [min_value]
        result.extend(self.sort_recursive(data[1:]))
        return result

    def sort_iterative_alt(self, data):
        if data is None:
            raise TypeError
        if len(data) < 2:
            return data
        min_value = sys.maxsize
        temp = 0
        for i in range(len(data)):
            self._swap(data, i, i+self._find_min_index(data[i:]))
        return data

    def _find_min_index(self, data):
        temp = 0
        for i in range(len(data)):
            if data[i] < data[temp]:
                temp = i
        return temp

    def _swap(self, data, i, j):
        if i != j:
            data[i], data[j] = data[j], data[i]
        return data


class TestSelectionSort(object):

    def test_selection_sort(self, func):
        print('None input')
        assert_raises(TypeError, func, None)

        print('Empty input')
        assert_equal(func([]), [])

        print('One element')
        assert_equal(func([5]), [5])

        print('Two or more elements')
        data = [5, 1, 7, 2, 6, -3, 5, 7, -10]
        assert_equal(func(data), sorted(data))

        print('Success: test_selection_sort\n')


def main():
    test = TestSelectionSort()
    selection_sort = SelectionSort()
    test.test_selection_sort(selection_sort.sort)
    try:
        test.test_selection_sort(selection_sort.sort_recursive)
        test.test_selection_sort(selection_sort.sort_iterative_alt)
    except NameError:
        # Alternate solutions are only defined
        # in the solutions file
        pass


if __name__ == '__main__':
    main()