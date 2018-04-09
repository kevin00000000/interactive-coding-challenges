from nose.tools import assert_equal


class Math(object):

    def fib_recursive(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib_recursive(n-1) + self.fib_recursive(n-2)

    def fib_iterative(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        first = 0
        second = 1
        for _ in range(n-1):
            temp = second
            second = first + second
            first = temp
        return second
        

    def fib_dynamic(self, n):
        result = [0, 1]
        for i in range(2, n+1):
            result.append(result[i-2] + result[i-1])
        return result[n]


class TestFib(object):

    def test_fib(self, func):
        result = []
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for i in range(len(expected)):
            result.append(func(i))
        assert_equal(result, expected)
        print('Success: test_fib')


def main():
    test = TestFib()
    math = Math()
    test.test_fib(math.fib_recursive)
    test.test_fib(math.fib_dynamic)
    test.test_fib(math.fib_iterative)


if __name__ == '__main__':
    main()