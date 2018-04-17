from nose.tools import assert_equal, assert_raises
import sys


class Matrix(object):

    def __init__(self, first, second):
        self.first = first
        self.second = second

# top-down
class MatrixMultiplicationCost(object):

    def __init__(self):
        self.temp_result = []

    def _init_result(self, n):
        for i in range(n):
            self.temp_result.append([])
            for j in range(n):
                self.temp_result[i].append(None)

    def find_min_cost(self, array):
        if array is None:
            raise TypeError("param is None")
        if len(array) < 2:
            return 0
        self._init_result(len(array))
        min_matrix, min_count = self._find_min_cost(array, 0, len(array)-1)
        return min_count

    def _find_min_cost(self, array, start, end):
        if self.temp_result[start][end] != None:
            return self.temp_result
        min_count = sys.maxsize
        min_matrix = None
        if end - start == 1:
            min_count = array[start].first*array[start].second*array[end].second
            min_matrix = Matrix(array[start].first, array[end].second)
            return min_matrix, min_count
        for i in range(start, end):
            temp_matrix = None
            temp_count = 0
            temp_matrix1 = None
            temp_count1 = 0
            if i == start:
                temp_matrix, temp_count = self._find_min_cost(array, start+1, end)
                temp_count += array[start].first * array[start].second * temp_matrix.second
                temp_matrix = Matrix(array[start].first, temp_matrix.second)
            elif i == end - 1:
                temp_matrix, temp_count = self._find_min_cost(array, start, end-1)
                temp_count += temp_matrix.first * array[end].first * array[end].second
                temp_matrix = Matrix(temp_matrix.first, array[end].second)
            else:
                temp_matrix, temp_count = self._find_min_cost(array, start, start+(i-start))
                temp_matrix1, temp_count1 = self._find_min_cost(array, start+(i-start+1), end)
                temp_count += temp_count1 + (temp_matrix.first * temp_matrix.second * temp_matrix1.second)
                temp_matrix = Matrix(temp_matrix.first, temp_matrix1.second)
            if temp_count < min_count:
                min_count = temp_count
                min_matrix = temp_matrix
        self.temp_result[start][end] = (min_matrix, min_count)
        return min_matrix, min_count


# bottom-up
class MatrixMultiplicationCostBottomUp(object):

    def __init__(self):
        self.results = []
        self.results_count = []

    def _init_result(self, n):
        for _ in range(n):
            self.results.append([])
            self.results_count.append([])
            for __ in range(n):
                self.results[_].append(None)
                self.results_count[_].append(sys.maxsize)

    def find_min_cost(self, array):
        if array is None:
            raise TypeError("param is None")
        if len(array) < 2:
            return 0
        self._init_result(len(array))
        self._fill_result(array)
        return self.results_count[0][len(array)-1]

    def _fill_result(self, array):
        n = len(array)
        for i in range(n-1, -1, -1):
            for j in range(n):
                if i > j:
                    self.results[i][j] = None
                    self.results_count[i][j] = sys.maxsize
                    continue
                if i == j:
                    self.results[i][j] = array[i]
                    self.results_count[i][i] = 0
                    continue
                for _ in range(j-i):
                    temp_matrix = Matrix(self.results[i][i+_].first, self.results[i+_+1][j].second)
                    temp_count = self.results_count[i][i+_] + self.results_count[i+_+1][j] + self.results[i][i+_].first*self.results[i][i+_].second*self.results[i+_+1][j].second
                    if temp_count < self.results_count[i][j]:
                        self.results[i][j] = temp_matrix
                        self.results_count[i][j] = temp_count



class TestMatrixMultiplicationCost(object):

    def test_find_min_cost(self):
        matrix_mult_cost = MatrixMultiplicationCostBottomUp()
        assert_raises(TypeError, matrix_mult_cost.find_min_cost, None)
        assert_equal(matrix_mult_cost.find_min_cost([]), 0)
        matrices = [Matrix(2, 3),
                    Matrix(3, 6),
                    Matrix(6, 4),
                    Matrix(4, 5)]
        expected_cost = 124
        assert_equal(matrix_mult_cost.find_min_cost(matrices), expected_cost)
        print('Success: test_find_min_cost')


def main():
    test = TestMatrixMultiplicationCost()
    test.test_find_min_cost()


if __name__ == '__main__':
    main()