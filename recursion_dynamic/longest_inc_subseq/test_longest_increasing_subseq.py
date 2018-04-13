from nose.tools import assert_equal, assert_raises


class Subsequence(object):

    def __init__(self):
        self.results = []
        self.result_seq = []
    
    def longest_inc_subseq(self, seq):
        if seq is None:
            raise TypeError("param is None")
        if not seq:
            return []
        self._init_result(len(seq))
        self._fill_result(seq)
        return self.result_seq[len(seq)]
    
    def _init_result(self, length):
        for _ in range(length+1):
            self.results.append(0)
            self.result_seq.append([])

    def _fill_result(self, seq):
        for i in range(len(seq)+1):
            if i == 0:
                self.results[i] = 0
                self.result_seq = []
                continue
            if self.results[i-1]+1


class TestLongestIncreasingSubseq(object):

    def test_longest_increasing_subseq(self):
        subseq = Subsequence()
        assert_raises(TypeError, subseq.longest_inc_subseq, None)
        assert_equal(subseq.longest_inc_subseq([]), [])
        seq = [3, 4, -1, 0, 6, 2, 3]
        expected = [-1, 0, 2, 3]
        assert_equal(subseq.longest_inc_subseq(seq), expected)
        print('Success: test_longest_increasing_subseq')


def main():
    test = TestLongestIncreasingSubseq()
    test.test_longest_increasing_subseq()


if __name__ == '__main__':
    main()