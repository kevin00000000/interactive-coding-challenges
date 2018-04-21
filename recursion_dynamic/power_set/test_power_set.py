from nose.tools import assert_equal


class Combinatoric(object):
    def __init__(self):
        self.result = []

    def find_power_set(self, input_set):
        if input_set is None:
            raise TypeError("param is None")
        if not input_set:
            return ['']
        self._init_result(len(input_set))
        self._fill_result(input_set)
        temp_set = set()
        temp_set.add('')
        l = list(sorted(self.result[len(input_set)]-temp_set))
        l.append('')
        return l
    
    def _init_result(self, n):
        for _ in range(n+1):
            self.result.append(set())

    def _fill_result(self, input_set):
        for i in range(len(input_set)+1):
            if i == 0:
                self.result[i].add('')
                continue
            self.result[i] |= self.result[i-1]
            for item in self.result[i-1]:
                self.result[i].add(item + input_set[i-1])


class TestPowerSet(object):

    def test_power_set(self):
        input_set = ''
        expected = ['']
        self.run_test(input_set, expected)
        input_set = 'a'
        expected = ['a', '']
        self.run_test(input_set, expected)
        input_set = 'ab'
        expected = ['a', 'ab', 'b', '']
        self.run_test(input_set, expected)
        input_set = 'abc'
        expected = ['a', 'ab', 'abc', 'ac',
                    'b', 'bc', 'c', '']
        self.run_test(input_set, expected)
        input_set = 'aabc'
        expected = ['a', 'aa', 'aab', 'aabc', 
                    'aac', 'ab', 'abc', 'ac', 
                    'b', 'bc', 'c', '']
        self.run_test(input_set, expected)
        print('Success: test_power_set')

    def run_test(self, input_set, expected):
        combinatoric = Combinatoric()
        result = combinatoric.find_power_set(input_set)
        assert_equal(result, expected)


def main():
    test = TestPowerSet()
    test.test_power_set()


if __name__ == '__main__':
    main()