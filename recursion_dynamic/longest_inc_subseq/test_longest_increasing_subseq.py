from nose.tools import assert_equal, assert_raises


class Subsequence(object):

    def __init__(self):
        self.results = []
        self.result_seq = []
        self.max_index = 0
    
    def longest_inc_subseq(self, seq):
        if seq is None:
            raise TypeError("param is None")
        if not seq:
            return []
        self._init_result(len(seq))
        self._fill_result(seq)
        return self.result_seq[self.max_index]
    
    def _init_result(self, length):
        for _ in range(length+1):
            self.results.append(0)
            self.result_seq.append([])

    def _fill_result(self, seq):
        max_count = 0
        for i in range(len(seq)):
            if i == 0:
                self.results[i] = 1
                self.result_seq[i].append(seq[i])
                max_count = 1
                continue
            max_temp_result = 0
            max_j = 0
            for j in range(0, i):
                if seq[j] < seq[i] and self.results[j]+1 > max_temp_result:
                    max_temp_result = self.results[j]+1
                    max_j = j
            if not max_temp_result:
                self.results[i] = 1
                self.result_seq[i].append(seq[i])
            else:
                self.results[i] = max_temp_result
                self.result_seq[i].extend(self.result_seq[max_j])
                self.result_seq[i].append(seq[i])
            if self.results[i] > max_count:
                max_count = self.results[i]
                self.max_index = i



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