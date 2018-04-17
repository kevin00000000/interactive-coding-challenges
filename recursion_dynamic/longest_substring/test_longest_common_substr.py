from nose.tools import assert_equal, assert_raises


class StringCompare(object):

    def __init__(self):
        self.results = []
        self.results_seq = []
        self.longest_i = 0
        self.longest_j = 0

    def longest_common_substr(self, s1, s2):
        if s1 is None or s2 is None:
            raise TypeError("param is None")
        if len(s1) == 0 or len(s2) == 0:
            return ''
        self._init_result(len(s1), len(s2))
        self._fill_result(s1, s2)
        return ''.join(self.results_seq[self.longest_i][self.longest_j])

    def _init_result(self, n1, n2):
        for i in range(n1+1):
            self.results.append([])
            self.results_seq.append([])
            for _ in range(n2+1):
                self.results[i].append(0)
                self.results_seq[i].append([])

    def _fill_result(self, s1, s2):
        max_count = 0
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i == 0 or j == 0:
                    self.results[i][j] = 0
                    continue
                if s1[i-1] == s2[j-1]:
                    self.results[i][j] = self.results[i-1][j-1] + 1
                    self.results_seq[i][j].extend(self.results_seq[i-1][j-1])
                    self.results_seq[i][j].append(s1[i-1])
                else:
                    self.results[i][j] = 0
                if self.results[i][j] > max_count:
                    max_count = self.results[i][j]
                    self.longest_i = i
                    self.longest_j = j


class TestLongestCommonSubstr(object):

    def test_longest_common_substr(self):
        str_comp = StringCompare()
        assert_raises(TypeError, str_comp.longest_common_substr, None, None)
        assert_equal(str_comp.longest_common_substr('', ''), '')
        str0 = 'ABCDEFGHIJ'
        str1 = 'FOOBCDBCDE'
        expected = 'BCDE'
        assert_equal(str_comp.longest_common_substr(str0, str1), expected)
        print('Success: test_longest_common_substr')


def main():
    test = TestLongestCommonSubstr()
    test.test_longest_common_substr()


if __name__ == '__main__':
    main()