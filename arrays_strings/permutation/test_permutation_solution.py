from nose.tools import assert_equal


class  Permutations(object):
    def is_permutation(self, s1, s2):
        if s1 is None or s2 is None:
            return False
        l1 = list(s1)
        l1.sort()
        l2 = list(s2)
        l2.sort()
        return l1 == l2

class PermutationsAlt(object):
    def is_permutation(self, s1, s2):
        if s1 is None or s2 is None:
            return False
        d1 = {}
        d2 = {}
        for c in s1:
            d1[c] = d1.get(c, 0)+1
        for c in s2:
            d2[c] = d2.get(c, 0)+1
        return d1 == d2


class TestPermutation(object):

    def test_permutation(self, func):
        assert_equal(func(None, 'foo'), False)
        assert_equal(func('', 'foo'), False)
        assert_equal(func('Nib', 'bin'), False)
        assert_equal(func('act', 'cat'), True)
        assert_equal(func('a ct', 'ca t'), True)
        assert_equal(func('dog', 'doggo'), False)
        print('Success: test_permutation')


def main():
    test = TestPermutation()
    permutations = Permutations()
    test.test_permutation(permutations.is_permutation)
    try:
        permutations_alt = PermutationsAlt()
        test.test_permutation(permutations_alt.is_permutation)
    except NameError:
        # Alternate solutions are only defined
        # in the solutions file
        pass


if __name__ == '__main__':
    main()