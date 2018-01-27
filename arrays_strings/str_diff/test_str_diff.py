from nose.tools import assert_equal, assert_raises


class Solution(object):

    def find_diff(self, s, t):
        # TODO: Implement me
        if s is None or t is None:
            raise TypeError
        s_map = {}
        for v in s:
            s_map[v] = s_map.get(v, 0)+1
        for v in t:
            if v not in s_map:
                return v
            s_map[v] -= 1
            if(s_map[v] < 0):
                return v
        return None

    def find_diff_xor(self, s, t):
        # TODO: Implement me
        # 仅支持只有一个字符不一致的情形，利用了xor操作的特性已经对称性
        if s is None or t is None:
            raise TypeError
        result = 0
        for v in s:
            result ^= ord(v)
        for v in t:
            result ^= ord(s)
        return chr(result)

class TestFindDiff(object):

    def test_find_diff(self):
        solution = Solution()
        assert_raises(TypeError, solution.find_diff, None)
        assert_equal(solution.find_diff('abcd', 'abcde'), 'e')
        assert_equal(solution.find_diff('aaabbcdd', 'abdbacade'), 'e')
        print('Success: test_find_diff')


def main():
    test = TestFindDiff()
    test.test_find_diff()


if __name__ == '__main__':
    main()