from nose.tools import assert_equal

def validate_index(bit_func):
    def validate_index_wrapper(self, *args, **kwargs):
        for arg in args:
            if arg<0:
                raise ValueError
        return bit_func(self, *args, **kwargs)
    return validate_index_wrapper

class Bit(object):

    def __init__(self, number):
        # TODO: Implement me
        self.number = number

    @validate_index
    def get_bit(self, index):
        # TODO: Implement me
        return (self.number & (1<<index)) != 0

    @validate_index
    def set_bit(self, index):
        # TODO: Implement me
        return self.number | 1<<index

    @validate_index
    def clear_bit(self, index):
        # TODO: Implement me
        return self.number & ~(2**index)

    @validate_index
    def clear_bits_msb_to_index(self, index):
        # TODO: Implement me
        return self.number & 2**index-1

    @validate_index
    def clear_bits_index_to_lsb(self, index):
        # TODO: Implement me
        return self.number & ~(2**(index+1)-1)

    @validate_index
    def update_bit(self, index, value):
        # TODO: Implement me
        if value:
            return self.number | 2**index
        else:
            return self.number & ~(2**index)


class TestBit(object):

    def test_bit(self):
        number = int('10001110', base=2)
        bit = Bit(number)
        assert_equal(bit.get_bit(index=3), True)
        expected = int('10011110', base=2)
        assert_equal(bit.set_bit(index=4), expected)
        bit = Bit(number)
        expected = int('10000110', base=2)
        assert_equal(bit.clear_bit(index=3), expected)
        bit = Bit(number)
        expected = int('00000110', base=2)
        assert_equal(bit.clear_bits_msb_to_index(index=3), expected)
        bit = Bit(number)
        expected = int('10000000', base=2)
        assert_equal(bit.clear_bits_index_to_lsb(index=3), expected)
        bit = Bit(number)
        assert_equal(bit.update_bit(index=3, value=1), number)
        bit = Bit(number)
        expected = int('10000110', base=2)
        assert_equal(bit.update_bit(index=3, value=0), expected)
        bit = Bit(number)
        expected = int('10001111', base=2)
        assert_equal(bit.update_bit(index=0, value=1), expected)
        print('Success: test_bit')


def main():
    test = TestBit()
    test.test_bit()


if __name__ == '__main__':
    main()