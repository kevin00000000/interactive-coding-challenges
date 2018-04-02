from nose.tools import assert_equal, assert_raises

class Bits(object):
    MAX_BITS = 32
    def get_next_largest(self, num):
        if num is None or type(num) is not int:
            raise TypeError('invalid param')
        if num <= 0:
            raise ValueError("num can't be less than 0")
        count = self._get_one_num(num)
        while True:
            num += 1
            if self._get_one_num(num) == count:
                return num
        return 0

    def get_next_smallest(self, num):
        if num <= 0:
            raise ValueError("num can't be less than 0")
        count = self._get_one_num(num)
        while True:
            num -= 1
            if self._get_one_num(num) == count:
                return num
        return 0
    
    def _get_one_num(self, num):
        count = 0
        for x in range(0, self.MAX_BITS):
            if num & 1:
                count += 1
            num >>= 1
        return count

class BitsSolution(object):
    def get_next_largest(self, num):
        if num is None or type(num) is not int:
            raise TypeError('invalid param')
        if num <= 0:
            raise ValueError("num can't be less than 0")
        num_zero = 0
        num_one = 0
        num_copy = num
        while num_copy != 0 and num_copy & 1 == 0:
            num_zero += 1
            num_copy >>= 1
        while num_copy != 0 and num_copy & 1 == 1:
            num_one += 1
            num_copy >>= 1
        index = num_zero + num_one
        num |= 1<<index
        num &= ~((1<<index)-1)
        num |= (1<<(num_one-1))-1
        return num
    
    def get_next_smallest(self, num):
        if num is None or type(num) is not int:
            raise TypeError('invalid param')
        if num <= 0:
            raise ValueError("num can't be less than 0")
        num_one = 0
        num_zero = 0
        num_copy = num
        while num_copy != 0 and num_copy & 1 == 1:
            num_one += 1
            num_copy >>= 1
        while num_copy != 0 and num_copy & 1 == 0:
            num_zero += 1
            num_copy >>= 1
        if num_copy != 0:
            index = num_one + num_zero
            num &= ~((1<<index))
            num &= ~((1<<index) - 1)
            num |= ((1<<(num_one+1))-1)<<(num_zero-1)
            return num
        else:
            raise ValueError("have no next smallest num")

class TestBits(object):

    def test_get_next_largest(self):
        bits = BitsSolution()
        assert_raises(Exception, bits.get_next_largest, None)
        assert_raises(Exception, bits.get_next_largest, 0)
        assert_raises(Exception, bits.get_next_largest, -1)
        num = int('011010111', base=2)
        expected = int('011011011', base=2)
        assert_equal(bits.get_next_largest(num), expected)
        print('Success: test_get_next_largest')

    def test_get_next_smallest(self):
        bits = BitsSolution()
        assert_raises(Exception, bits.get_next_smallest, None)
        assert_raises(Exception, bits.get_next_smallest, 0)
        assert_raises(Exception, bits.get_next_smallest, -1)
        num = int('011010111', base=2)
        expected = int('011001111', base=2)
        assert_equal(bits.get_next_smallest(num), expected)
        print('Success: test_get_next_smallest')

def main():
    test = TestBits()
    test.test_get_next_largest()
    test.test_get_next_smallest()


if __name__ == '__main__':
    main()