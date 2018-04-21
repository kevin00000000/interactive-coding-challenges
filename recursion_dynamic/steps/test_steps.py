from nose.tools import assert_equal, assert_raises


class Steps(object):
    def __init__(self):
        self.results = []
    
    def count_ways(self, n):
        if n is None or type(n) is not int:
            raise TypeError("param is None")
        if n < 0:
            raise TypeError("n is smaller than zero")
        self._init_result(n)
        self._fill_result(n)
        return self.results[n]

    def _init_result(self, n):
        for _ in range(n+1):
            self.results.append(0)
        
    def _fill_result(self, n):
        for i in range(n+1):
            if i == 0 or i == 1:
                self.results[i] = 1
                continue
            if i == 2:
                self.results[i] = 2
                continue
            self.results[i] = self.results[i-3] + self.results[i-2] + self.results[i-1]
            


class TestSteps(object):

    def test_steps(self):
        steps = Steps()
        assert_raises(TypeError, steps.count_ways, None)
        assert_raises(TypeError, steps.count_ways, -1)
        assert_equal(steps.count_ways(0), 1)
        assert_equal(steps.count_ways(1), 1)
        assert_equal(steps.count_ways(2), 2)
        assert_equal(steps.count_ways(3), 4)
        assert_equal(steps.count_ways(4), 7)
        assert_equal(steps.count_ways(10), 274)
        print('Success: test_steps')


def main():
    test = TestSteps()
    test.test_steps()


if __name__ == '__main__':
    main()