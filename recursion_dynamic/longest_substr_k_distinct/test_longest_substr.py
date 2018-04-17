from nose.tools import assert_equal, assert_raises


class Solution(object):
    
    def __init__(self):
        self.results = []
        self.longest_count = 0
    
    def longest_substr(self, s, k):
        if s is None:
            raise TypeError("param is None")
        if len(s) == 0:
            return 0
        n = len(s)
        self._init_result(n, k)
        self._fill_result(s, k)
        return self.longest_count
    
    def _init_result(self, n, k):
        for _ in range(n):
            self.results.append(0)
    
    def _fill_result(self, s, k):
        char_to_index_map = {}
        for index, char in enumerate(s):
            char_to_index_map[char] = index
            if index == 0:
                self.results[index] = 1
                self.longest_count = 1
                continue
            if len(char_to_index_map.keys()) <= k:
                self.results[index] = self.results[index-1] + 1
            else:
                min_index = min(char_to_index_map.values())
                self.results[index] = index - min_index
                del char_to_index_map[s[min_index]]
            if self.results[index] > self.longest_count:
                self.longest_count = self.results[index]
            


class TestSolution(object):

    def test_longest_substr(self):
        solution = Solution()
        assert_raises(TypeError, solution.longest_substr, None)
        assert_equal(solution.longest_substr('', k=3), 0)
        assert_equal(solution.longest_substr('aaaaaabbbbb', k=3), 11)
        assert_equal(solution.longest_substr('abcabcdefgghiij', k=3), 6)
        assert_equal(solution.longest_substr('abcabcdefgghighij', k=3), 7)
        print('Success: test_longest_substr')


def main():
    test = TestSolution()
    test.test_longest_substr()


if __name__ == '__main__':
    main()