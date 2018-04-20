from nose.tools import assert_equal, assert_raises


class Parentheses(object):
    def __init__(self):
        self.results = []
        self.result_counts = []

    def find_pair(self, num):
        if num is None or type(num) is not int:
            raise TypeError("param is None or is not int")
        if num < 0:
            raise ValueError("num smaller than zero")
        if num == 0:
            return []
        self._init_result(num)
        self._fill_result(num)
        return list(sorted(self.results[num]))
    
    def _init_result(self, num):
        for _ in range(num+1):
            self.results.append(set())
            self.result_counts.append(0)

    def _fill_result(self, num):
        for i in range(1, num+1):
            if i == 1:
                self.result_counts[i] = 1
                self.results[i].add("()")
            else:
                self.result_counts[i] = self.result_counts[i-1] * 3 - 1
                for item in self.results[i-1]:
                    self.results[i].add('(' + item + ')')  
                for item in self.results[i-1]:
                    self.results[i].add('()' + item)
                for item in self.results[i-1]:
                    self.results[i].add(item + '()')      


class TestPairParentheses(object):

    def test_pair_parentheses(self):
        parentheses = Parentheses()
        assert_raises(TypeError, parentheses.find_pair, None)
        assert_raises(ValueError, parentheses.find_pair, -1)
        assert_equal(parentheses.find_pair(0), [])
        assert_equal(parentheses.find_pair(1), ['()'])
        assert_equal(parentheses.find_pair(2), ['(())',
                                                '()()'])
        assert_equal(parentheses.find_pair(3), ['((()))',
                                                '(()())',
                                                '(())()',
                                                '()(())',
                                                '()()()'])
        print('Success: test_pair_parentheses')


def main():
    test = TestPairParentheses()
    test.test_pair_parentheses()


if __name__ == '__main__':
    main()