from nose.tools import assert_equal, assert_raises

class Array(object):
    def merge_into(self, source, dest, source_end_index, dest_end_index):
        if source is None or dest is None:
            raise TypeError
        if source_end_index < 0 or dest_end_index < 0:
            raise ValueError
        if len(dest) == 0:
            return source
        source_end_index -= 1
        dest_end_index -= 1
        none_last_index = len(source)-1
        while dest_end_index >= 0 and source_end_index >= 0:
            if source[source_end_index] > dest[dest_end_index]:
                source[source_end_index], source[none_last_index] = source[none_last_index], source[source_end_index]
                source_end_index -= 1
                none_last_index -= 1
            else:
                source[none_last_index] = dest[dest_end_index]
                none_last_index -= 1
                dest_end_index -= 1
        if source_end_index < 0:
            for i in range(dest_end_index+1):
                source[i] = dest[i]
        return source


class TestArray(object):

    def test_merge_into(self):
        array = Array()
        assert_raises(TypeError, array.merge_into, None, None, None, None)
        assert_raises(ValueError, array.merge_into, [1], [2], -1, -1)
        a = [1, 2, 3]
        assert_equal(array.merge_into(a, [], len(a), 0), [1, 2, 3])
        a = [1, 2, 3]
        assert_equal(array.merge_into(a, [], len(a), 0), [1, 2, 3])
        a = [1,  3,  5,  7,  9,  None,  None,  None]
        b = [4,  5,  6]
        expected = [1, 3, 4, 5, 5, 6, 7, 9]
        assert_equal(array.merge_into(a, b, 5, len(b)), expected)
        print('Success: test_merge_into')


def main():
    test = TestArray()
    test.test_merge_into()


if __name__ == '__main__':
    main()