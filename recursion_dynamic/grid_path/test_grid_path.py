from nose.tools import assert_equal


class Grid(object):

    def find_path(self, maze):
        if maze is None:
            return None
        if not maze or not maze[0]:
            return None
        self._init_result(len(maze), len(maze[0]))
        self._fill_result(maze, len(maze), len(maze[0]))
        return self.result[0][0]

    def _init_result(self, row, column):
        self.result = [[None]*column for _ in range(row)]

    def _fill_result(self, maze, row, column):
        for r in range(row-1, -1, -1):
            for c in range(column-1, -1, -1):
                if r == row-1 and c == column-1:
                    self.result[r][c] = [(r, c)]
                else:
                    if maze[r][c] == 0:
                        self.result[r][c] = None
                    else:
                        if c != column-1:
                            if self.result[r][c+1] is not None:
                                self.result[r][c] = [(r, c)]
                                self.result[r][c].extend(self.result[r][c+1])
                            else:
                                self.result[r][c] = None
                        if r != row-1 and self.result[r][c] is None:
                            if self.result[r+1][c] is not None:
                                self.result[r][c] = [(r, c)]
                                self.result[r][c].extend(self.result[r+1][c])
                            else:
                                self.result[r][c] = None
                    


class TestGridPath(object):

    def test_grid_path(self):
        grid = Grid()
        assert_equal(grid.find_path(None), None)
        assert_equal(grid.find_path([[]]), None)
        max_rows = 8
        max_cols = 4
        matrix = [[1] * max_cols for _ in range(max_rows)]
        matrix[1][1] = 0
        matrix[2][2] = 0
        matrix[3][0] = 0
        matrix[4][2] = 0
        matrix[5][3] = 0
        matrix[6][1] = 0
        matrix[6][3] = 0
        matrix[7][1] = 0
        result = grid.find_path(matrix)
        expected = [(0, 0), (1, 0), (2, 0),
                    (2, 1), (3, 1), (4, 1),
                    (5, 1), (5, 2), (6, 2),
                    (7, 2), (7, 3)]
        assert_equal(result, expected)
        matrix[7][2] = 0
        result = grid.find_path(matrix)
        assert_equal(result, None)
        print('Success: test_grid_path')


def main():
    test = TestGridPath()
    test.test_grid_path()


if __name__ == '__main__':
    main()