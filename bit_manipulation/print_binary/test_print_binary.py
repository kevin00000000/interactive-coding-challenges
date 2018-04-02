from nose.tools import assert_equal
import math

class Bits(object):
    def print_binary(self, num):
        if num is None:
            return 'ERROR'
        if num >= 1 or num <= 0:
            return 'ERROR'
        count = 0
        result = '0.'
        while count < 32:
            decimal, integer = math.modf(num*2)
            if integer == 1:
                result += "1"
            else:
                result += '0'
            count += 1
            if decimal == 0.0:
                break
            num = decimal
        if count >= 32:
            return 'ERROR'
        return result
            

class TestBits(object):

    def test_print_binary(self):
        bit = Bits()
        assert_equal(bit.print_binary(None), 'ERROR')
        assert_equal(bit.print_binary(0), 'ERROR')
        assert_equal(bit.print_binary(1), 'ERROR')
        num = 0.625
        expected = '0.101'
        assert_equal(bit.print_binary(num), expected)
        num = 0.987654321
        assert_equal(bit.print_binary(num), 'ERROR')
        print('Success: test_print_binary')


def main():
    test = TestBits()
    test.test_print_binary()


if __name__ == '__main__':
    main()