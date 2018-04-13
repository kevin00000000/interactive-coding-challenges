from nose.tools import assert_equal, assert_raises


class StringCompare(object):

    def __init__(self):
        self.results = []
        self.results_str = []
        self.i = 0
        self.j = 0
    
    def longest_common_subseq(self, str0, str1):
        if str0 is None or str1 is None:
            raise TypeError("param is None")
        if not len(str0) or not len(str1):
            return ''
        self._init_result(len(str0), len(str1))
        self._fill_result(str0, str1)
        return ''.join(self.results_str[self.i][self.j])
    
    def _init_result(self, len1, len2):
        for i in range(len1+1):
            self.results.append([])
            self.results_str.append([])
            for _ in range(len2+1):
                self.results[i].append(0)
                self.results_str[i].append([])
    
    def _fill_result(self, str0, str1):
        len0 = len(str0)
        len1 = len(str1)
        max_value = 0
        for i in range(len0+1):
            for j in range(len1+1):
                if not i or not j:
                    self.results[i][j] = 0
                    self.results_str[i][j] = []
                    continue
                if str0[i-1] == str1[j-1]:
                    self.results[i][j] = self.results[i-1][j-1] + 1
                    self.results_str[i][j].extend(self.results_str[i-1][j-1])
                    self.results_str[i][j].append(str0[i-1])
                    if self.results[i][j] > max_value:
                        self.i = i
                        self.j = j
                        max_value = self.results[i][j]
                else:
                    self.results[i][j] = 0
                    self.results_str[i][j] = []
                


class TestLongestCommonSubseq(object):

    def test_longest_common_subseq(self):
        str_comp = StringCompare()
        assert_raises(TypeError, str_comp.longest_common_subseq, None, None)
        assert_equal(str_comp.longest_common_subseq('', ''), '')
        str0 = 'ABCDEFGHIJ'
        str1 = 'FOOBCDBCDE'
        expected = 'BCDE'
        assert_equal(str_comp.longest_common_subseq(str0, str1), expected)
        print('Success: test_longest_common_subseq')


def main():
    test = TestLongestCommonSubseq()
    test.test_longest_common_subseq()


if __name__ == '__main__':
    main()
