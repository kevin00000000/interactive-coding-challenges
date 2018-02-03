from nose.tools import assert_equal, assert_raises

class SortedMatrix(object):
    
    def find_val(self, matrix, val):
        if matrix is None:
            raise TypeError
        if not matrix:
            return None
        return self._find_val(matrix, val, 0, len(matrix[0])-1)
    
    def _find_val(self, matrix, val, y, x):
        if x > len(matrix)-1:
            return None
        if y > len(matrix[0])-1:
            return None
        if matrix[y][x] > val:
            return self._find_val(matrix, val, y, x-1)
        elif matrix[y][x] < val:
            return self._find_val(matrix, val, y+1, x)
        else:
            return y, x
        


class TestSortedMatrix(object):

    def test_find_val(self):
        matrix = [[20, 40, 63, 80],
                  [30, 50, 80, 90],
                  [40, 60, 110, 110],
                  [50, 65, 105, 150]]
        sorted_matrix = SortedMatrix()
        assert_raises(TypeError, sorted_matrix.find_val, None, None)
        assert_equal(sorted_matrix.find_val(matrix, 1000), None)
        assert_equal(sorted_matrix.find_val(matrix, 60), (2, 1))
        print('Success: test_find_val')


def main():
    test = TestSortedMatrix()
    test.test_find_val()


if __name__ == '__main__':
    main()