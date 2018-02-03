from nose.tools import assert_equal, assert_raises

class RadixSort(object):
    def sort(self, array, base=10):
        if array is None:
            raise TypeError
        if len(array) < 2:
            return array
        mod = 10
        over, array = self._sort(array, base, mod)
        while not over:
            mod *= 10
            over, array = self._sort(array, base, mod)
        return array
    
    def _sort(self, array, base, mod):
        over = True
        count = {}
        result = [0 for _ in range(len(array))]
        individual_count = [0 for _ in range(10)]
        mod_array = []
        for item in array:
            if item > mod:
                over = False
            num = item % mod
            num //= (mod//10)
            mod_array.append(num)
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        for index, value in enumerate(array):
            mod = mod_array[index]
            pos = 0
            for i in range(mod):
                pos += count.get(i, 0)
            pos += individual_count[mod]
            individual_count[mod] += 1
            result[pos] = value
        return over, result
        
    def sort_solution(self, array, base=10):
        if array is None:
            raise TypeError
        if not array:
            return []
        max_element = max(array)
        max_digits = len(str(abs(max_element)))
        curr_array = array
        for digit in range(max_digits):
            buckets = [[] for _ in range(base)]
            for item in curr_array:
                buckets[(item//(base**digit))%base].append(item)
            curr_array = []
            for bucket in buckets:
                curr_array.extend(bucket)
        return curr_array

class TestRadixSort(object):

    def test_sort(self):
        radix_sort = RadixSort()
        assert_raises(TypeError, radix_sort.sort, None)
        assert_equal(radix_sort.sort([]), [])
        array = [128, 256, 164, 8, 2, 148, 212, 242, 244]
        expected = [2, 8, 128, 148, 164, 212, 242, 244, 256]
        assert_equal(radix_sort.sort(array), expected)
        print('Success: test_sort')


def main():
    test = TestRadixSort()
    test.test_sort()


if __name__ == '__main__':
    main()