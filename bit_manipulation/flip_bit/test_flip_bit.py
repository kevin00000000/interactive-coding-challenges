from nose.tools import assert_equal, assert_raises

class Bits(object):
    MAX_BITS = 32

    def flip_bit(self, num):
        if num is None:
            raise TypeError("Invalid argument")
        if num == -1:
            return self.MAX_BITS
        if num == 0:
            return 1
        seen = self._build_seen_list(num)
        max_result = 0
        looking_for = 0
        for index, count in enumerate(seen):
            result = 0
            if looking_for == 1:
                looking_for = 0
                continue
            if index == 0:
                if count != 0:
                    try:
                        result = seen[index+1]+1
                    except IndexError:
                        result = 1
            elif index == len(seen)-1:
                result = seen[index-1]+1
            else:
                if count == 1:
                    result = seen[index+1]+seen[index-1]+1
                else:
                    result = max(seen[index+1], seen[index-1]) + 1
            if result > max_result:
                max_result = result
            looking_for = 1 if looking_for == 0 else 0
        return max_result

    def _build_seen_list(self, num):
        seen = []
        looking_for = 0
        count = 0
        for _ in range(0, self.MAX_BITS):
            if num & 1 == 0:
                if looking_for == 0:
                    count += 1
                else:
                    seen.append(count)
                    count = 1
                    looking_for = 0
            else:
                if looking_for == 0:
                    seen.append(count)
                    count = 1

                    looking_for = 1
                else:
                    count += 1
            num >>= 1
        seen.append(count)
        return seen


class TestBits(object):

    def test_flip_bit(self):
        bits = Bits()
        assert_raises(TypeError, bits.flip_bit, None)
        assert_equal(bits.flip_bit(0), 1)
        assert_equal(bits.flip_bit(-1), bits.MAX_BITS)
        num = int('00001111110111011110001111110000', base=2)
        expected = 10
        assert_equal(bits.flip_bit(num), expected)
        num = int('00000100111011101111100011111011', base=2)
        expected = 9
        assert_equal(bits.flip_bit(num), expected)
        num = int('00010011101110111110001111101111', base=2)
        expected = 10
        assert_equal(bits.flip_bit(num), expected)
        print('Success: test_print_binary')


def main():
    test = TestBits()
    test.test_flip_bit()


if __name__ == '__main__':
    main()