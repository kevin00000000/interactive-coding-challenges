from nose.tools import assert_equal, assert_raises
from collections import OrderedDict

class Anagram(object):

    def group_anagrams(self, items):
        if items is None:
            raise TypeError
        if not items:
            return items
        ordered_dict = OrderedDict()
        for item in items:
            sorted_chars = tuple(sorted(item))
            if sorted_chars in ordered_dict:
                ordered_dict[sorted_chars].append(item)
            else:
                ordered_dict[sorted_chars] = [item]
        result = []
        for value in ordered_dict.values():
            result.extend(value)
        return result

class TestAnagrams(object):

    def test_group_anagrams(self):
        anagram = Anagram()
        assert_raises(TypeError, anagram.group_anagrams, None)
        data = ['ram', 'act', 'arm', 'bat', 'cat', 'tab']
        expected = ['ram', 'arm', 'act', 'cat', 'bat', 'tab']
        assert_equal(anagram.group_anagrams(data), expected)

        print('Success: test_group_anagrams')


def main():
    test = TestAnagrams()
    test.test_group_anagrams()


if __name__ == '__main__':
    main()