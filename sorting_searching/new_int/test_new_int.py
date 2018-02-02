from nose.tools import assert_equal, assert_raises
from bitstring import BitArray  # Run pip install bitstring


class Bits(object):

    def new_int(self, array, max_size):
        if not array:
            raise TypeError('array cannot be None or empty')
        base = max_size-32
        bit_vector = BitArray(32)
        for item in array:
            bit_vector[item-base] = True
        for index, item in enumerate(bit_vector):
            if not item:
                return index+base
        return None

class TestBits(object):

    def test_new_int(self):
        bits = Bits()
        max_size = 32
        assert_raises(TypeError, bits.new_int, None, max_size)
        assert_raises(TypeError, bits.new_int, [], max_size)
        data = [item for item in range(30)]
        data.append(31)
        assert_equal(bits.new_int(data, max_size), 30)
        data = [item for item in range(32)]
        assert_equal(bits.new_int(data, max_size), None)
        data = [item for item in range(1, 31)]
        data.append(32)
        assert_equal(bits.new_int(data, 33), 31)
        print('Success: test_find_int_excluded_from_input')


def main():
    test = TestBits()
    test.test_new_int()


if __name__ == '__main__':
    main()