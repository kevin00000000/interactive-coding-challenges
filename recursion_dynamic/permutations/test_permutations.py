from nose.tools import assert_equal


class Permutations(object):
    def __init__(self):
        self.result = []

    def find_permutations(self, string):
        if string is None or type(string) is not str:
            return None
        if not string:
            return ''
        array = [_ for _ in string]
        self._find_permutations(array, 0, len(string)-1)
        return list(sorted(set(self.result)))
    
    def _find_permutations(self, array, start, end):
        if start == end:
            self.result.append(''.join(array))
            return
        for i in range(start, end+1):
            array[start], array[i] = array[i], array[start]
            self._find_permutations(array, start+1, end)
            array[i], array[start] = array[start], array[i]


class TestPermutations(object):

    def test_permutations(self):
        permutations = Permutations()
        assert_equal(permutations.find_permutations(None), None)
        assert_equal(permutations.find_permutations(''), '')
        string = 'AABC'
        expected = [
            'AABC', 'AACB', 'ABAC', 'ABCA',
            'ACAB', 'ACBA', 'BAAC', 'BACA',
            'BCAA', 'CAAB', 'CABA', 'CBAA'
        ]
        assert_equal(permutations.find_permutations(string), expected)
        print('Success: test_permutations')


def main():
    test = TestPermutations()
    test.test_permutations()


if __name__ == '__main__':
    main()