from nose.tools import assert_equal, assert_raises


class Solution(object):
    
    def fizz_buzz(self, num):
        if num is None:
            raise TypeError
        if num < 1:
            raise ValueError
        return ["Fizz"*(n%3==0)+"Buzz"*(n%5==0) or str(n) for n in range(1, num+1)]


class TestFizzBuzz(object):

    def test_fizz_buzz(self):
        solution = Solution()
        assert_raises(TypeError, solution.fizz_buzz, None)
        assert_raises(ValueError, solution.fizz_buzz, 0)
        expected = [
            '1',
            '2',
            'Fizz',
            '4',
            'Buzz',
            'Fizz',
            '7',
            '8',
            'Fizz',
            'Buzz',
            '11',
            'Fizz',
            '13',
            '14',
            'FizzBuzz'
        ]
        assert_equal(solution.fizz_buzz(15), expected)
        print('Success: test_fizz_buzz')


def main():
    test = TestFizzBuzz()
    test.test_fizz_buzz()


if __name__ == '__main__':
    main()