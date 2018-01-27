from nose.tools import assert_equal, assert_raises
class Solution(object):

    def two_sum(self, nums, val):
        #TODO: Implement me
        if nums is None or val is None:
            raise TypeError
        if not nums:
            raise ValueError
        cache = {}
        for index, value in enumerate(nums):
            if cache.get(val-value):
                return [cache[val-value], index]
            else:
                cache[value] = index
        return None

class TestTwoSum(object):

    def test_two_sum(self):
        solution = Solution()
        assert_raises(TypeError, solution.two_sum, None, None)
        assert_raises(ValueError, solution.two_sum, [], 0)
        target = 7
        nums = [1, 3, 2, -7, 5]
        expected = [2, 4]
        assert_equal(solution.two_sum(nums, target), expected)
        print('Success: test_two_sum')


def main():
    test = TestTwoSum()
    test.test_two_sum()


if __name__ == '__main__':
    main()