from nose.tools import assert_equal, assert_raises


class Item(object):

    def __init__(self, label, value, weight):
        self.label = label
        self.value = value
        self.weight = weight

    def __repr__(self):
        return self.label + ' v:' + str(self.value) + ' w:' + str(self.weight)


class Knapsack(object):

    def __init__(self):
        self.results = []
    
    def fill_knapsack(self, items, total_weight):
        if items is None or total_weight is None:
            raise TypeError("param is None")
        if total_weight == 0:
            return 0
        self._init_results(items, total_weight)
        self._fill_knapsack(items, total_weight)
        return self.results[len(items)][total_weight]

    def _init_results(self, items, total_weight):
        for i in range(len(items)+1):
            self.results.append([])
            for _ in range(total_weight+1):
                self.results[i].append(0)

    def _fill_knapsack(self, items, total_weight):
        for i in range(len(items)+1):
            for t in range(total_weight+1):
                if t == 0 or i == 0:
                    self.results[i][t] = 0
                    continue
                if items[i-1].weight <= t:
                    self.results[i][t] = max(items[i-1].value + self.results[i][t-items[i-1].weight], self.results[i-1][t])
                else:
                    self.results[i][t] = self.results[i-1][t]


class TestKnapsack(object):

    def test_knapsack(self):
        knapsack = Knapsack()
        assert_raises(TypeError, knapsack.fill_knapsack, None, None)
        assert_equal(knapsack.fill_knapsack(0, 0), 0)
        items = []
        items.append(Item(label='a', value=1, weight=1))
        items.append(Item(label='b', value=3, weight=2))
        items.append(Item(label='c', value=7, weight=4))
        total_weight = 8
        expected_value = 14
        results = knapsack.fill_knapsack(items, total_weight)
        total_weight = 7
        expected_value = 11
        results = knapsack.fill_knapsack(items, total_weight)
        assert_equal(results, expected_value)
        print('Success: test_knapsack')

def main():
    test = TestKnapsack()
    test.test_knapsack()


if __name__ == '__main__':
    main()