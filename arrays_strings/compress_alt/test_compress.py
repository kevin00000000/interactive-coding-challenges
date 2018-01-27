from nose.tools import assert_equal


def compress_string(string):
    if string is None:
        return None
    if len(string) == 0:
        return ''
    s = string[0]
    count = 0
    result = []
    for c in string:
        if c == s:
            count += 1
        else:
            result.append((s, count))
            s = c
            count = 1
    result.append((s, count))
    result_string = ''.join([s*count if count<=2 else s+str(count) for s, count in result])
    return result_string if len(result_string)<len(string) else string




class TestCompress(object):

    def test_compress(self, func):
        assert_equal(func(None), None)
        assert_equal(func(''), '')
        assert_equal(func('AABBCC'), 'AABBCC')
        assert_equal(func('AAABCCDDDD'), 'A3BCCD4')
        assert_equal(func('aaBCCEFFFFKKMMMMMMP taaammanlaarrrr seeeeeeeeek tooo'), 'aaBCCEF4KKM6P ta3mmanlaar4 se9k to3')
        print('Success: test_compress')


def main():
    test = TestCompress()
    test.test_compress(compress_string)


if __name__ == '__main__':
    main()