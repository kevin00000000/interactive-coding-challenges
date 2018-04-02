from nose.tools import assert_equal

class Bits(object):
    def insert_m_into_n(self, m, n, i, j):
        if m is None or n is None or i is None or j is None:
            raise TypeError('param is None')
        if i > j:
            raise ValueError("invalid param")
        count = j - i + 1
        m &= ((1<<count)-1)
        n &= ~(((1<<count)-1)<<i)
        m <<= i
        return m | n

class TestBit(object):

    def test_insert_m_into_n(self):
        n = int('0000010000111101', base=2)
        m = int('0000000000010011', base=2)
        expected = int('0000010001001101', base=2)
        bits = Bits()
        assert_equal(bits.insert_m_into_n(m, n, i=2, j=6), expected)
        print('Success: test_insert_m_into_n')


def main():
    test = TestBit()
    test.test_insert_m_into_n()


if __name__ == '__main__':
    main()