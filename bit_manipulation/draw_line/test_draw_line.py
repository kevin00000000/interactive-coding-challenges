from nose.tools import assert_equal

class BitsScreen(object):
    def draw_line(self, screen, width, x1, x2):
        if None in (screen, width, x1, x2):
            raise TypeError('Invalid argument')
        if not screen or not width:
            raise ValueError('Invalid argument:Empty screen or width')
        MAX_BIT_VALUE = len(screen) * 8
        if x1<0 or x2<0 or x1>=MAX_BIT_VALUE or x2>=MAX_BIT_VALUE or x1 > x2:
            raise ValueError('Invalid argument: x1 or x2 out of bounds')
        start_bit = x1 % 8
        end_bit = x2 % 8
        first_full_byte = x1 // 8
        if start_bit != 0:
            first_full_byte += 1
        last_full_byte = x2 // 8
        if end_bit != 7:
            last_full_byte -=  1
        for byte in range(first_full_byte, last_full_byte+1):
            screen[byte] = int('11111111', 2)
        start_byte = x1 // 8
        end_byte = x2 // 8
        if start_byte == end_byte:
            left_mask = (1<<(8-start_bit)) - 1
            right_mast = ~((1<<(8-end_bit-1)) - 1)
            mask = left_mask & right_mast
            screen[start_byte] |= mask
        else:
            left_mask = (1<<(8-start_bit)) - 1
            right_mast = ~((1<<(8-end_bit-1)) - 1) & int('11111111', 2)
            screen[start_byte] |= left_mask
            screen[end_byte] |= right_mast
        
        
class TestBitsScreen(object):

    def test_draw_line(self):
        bits_screen = BitsScreen()
        screen = []
        for _ in range(20):
            screen.append(int('00000000', base=2))
        bits_screen.draw_line(screen, width=32, x1=68, x2=82)
        assert_equal(screen[8], int('00001111', base=2))
        assert_equal(screen[9], int('11111111', base=2))
        assert_equal(screen[10], int('11100000', base=2))
        bits_screen.draw_line(screen, width=32, x1=2, x2=6)
        assert_equal(screen[0], int('00111110', base=2))
        bits_screen.draw_line(screen, width=32, x1=10, x2=13)
        assert_equal(screen[1], int('00111100', base=2))
        print('Success: test_draw_line')


def main():
    test = TestBitsScreen()
    test.test_draw_line()


if __name__ == '__main__':
    main()