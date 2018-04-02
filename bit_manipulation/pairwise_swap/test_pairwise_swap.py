from nose.tools import assert_equal, assert_raises

class Bits(object):
    def pairwise_swap(self, num):
        if num <= 1:
            return num
        odd = num & 0b1010101010101010
        even = num & 0b0101010101010101
        odd >>= 1
        even <<= 1
        return odd | even

class TestBits(object):

    def test_pairwise_swap(self):
        bits = Bits()
        assert_equal(bits.pairwise_swap(0), 0)
        assert_equal(bits.pairwise_swap(1), 1)
        num = int('0000100111110110', base=2)
        expected = int('0000011011111001', base=2)
        assert_equal(bits.pairwise_swap(num), expected)
        assert_raises(TypeError, bits.pairwise_swap, None)
        
        print('Success: test_pairwise_swap')


def main():
    test = TestBits()
    test.test_pairwise_swap()


if __name__ == '__main__':
    main()