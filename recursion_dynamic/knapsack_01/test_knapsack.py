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
        self.results_value = []

    def fill_knapsack(self, items, total_weight):
        if items is None or total_weight is None:
            raise TypeError("param is None")
        if total_weight <= 0:
            return 0
        self._init_result(items, total_weight)
        self._fill_knapsack(items, total_weight)
        return self.results[len(items)][total_weight]

    def _init_result(self, items, total_weight):
        for _ in range(len(items)+1):
            self.results.append([])
            self.results_value.append([])
            for t in range(total_weight+1):
                self.results[_].append([])
                self.results_value[_].append(0)
    
    def _fill_knapsack(self, items, total_weight):
        for n in range(len(items)+1):
            for w in range(total_weight+1):
                if not w:
                    self.results[n][w].extend([])
                    self.results_value[n][w] = 0
                    continue
                if not n:
                    self.results[n][w].extend([])
                    self.results_value[n][w] = 0
                    continue
                if items[n-1].weight <= w:
                    if (items[n-1].value + self.results_value[n-1][w-items[n-1].weight]) >= self.results_value[n-1][w]:
                        self.results[n][w].append(items[n-1])
                        self.results[n][w].extend(self.results[n-1][w-items[n-1].weight])
                        self.results_value[n][w] = items[n-1].value + self.results_value[n-1][w-items[n-1].weight]
                    else:
                        self.results[n][w].extend(self.results[n-1][w])
                        self.results_value[n][w] = self.results_value[n-1][w]
                else:
                    self.results[n][w].extend(self.results[n-1][w])
                    self.results_value[n][w] = self.results_value[n-1][w]


class KnapsackTopDown(object):

    def __init__(self):
        self.results = []
    
    def fill_knapsack(self, items, total_weight):
        if items is None or total_weight is None:
            raise TypeError("param is None")
        if total_weight <= 0:
            return 0
        self._init_result(items, total_weight)
        return self._fill_knapsack(items, total_weight)

    def _init_result(self, items, total_weight):
        for i in range(len(items)+1):
            self.results.append([])
            for _ in range(total_weight+1):
                self.results[i].append(None)
    
    def _fill_knapsack(self, items, total_weight):
        length = len(items)
        if self.results[length][total_weight] is not None:
            return self.results[length][total_weight]
        if length == 0 or total_weight == 0:
            self.results[length][total_weight] = 0
            return 0
        if items[length-1].weight > total_weight:
            items.pop()
            item_copy = items.copy()
            self.results[length][total_weight] = self._fill_knapsack(item_copy, total_weight)
        else:
            item = items.pop()
            items_copy1 = items.copy()
            items_copy2 = items.copy()
            option1 = self._fill_knapsack(items_copy1, total_weight-item.weight) + item.value
            option2 = self._fill_knapsack(items_copy2, total_weight)
            if option1 >= option2:
                self.results[length][total_weight] = option1
            else:
                self.results[length][total_weight] = option2
        return self.results[length][total_weight]


class TestKnapsack(object):

    def test_knapsack_bottom_up(self):
        knapsack = Knapsack()
        assert_raises(TypeError, knapsack.fill_knapsack, None, None)
        assert_equal(knapsack.fill_knapsack(0, 0), 0)
        items = []
        items.append(Item(label='a', value=2, weight=2))
        items.append(Item(label='b', value=4, weight=2))
        items.append(Item(label='c', value=6, weight=4))
        items.append(Item(label='d', value=9, weight=5))
        total_weight = 8
        expected_value = 13
        results = knapsack.fill_knapsack(items, total_weight)
        assert_equal(results[0].label, 'd')
        assert_equal(results[1].label, 'b')
        total_value = 0
        for item in results:
            total_value += item.value
        assert_equal(total_value, expected_value)
        print('Success: test_knapsack_bottom_up')

    def test_knapsack_top_down(self):
        knapsack = KnapsackTopDown()
        assert_raises(TypeError, knapsack.fill_knapsack, None, None)
        assert_equal(knapsack.fill_knapsack(0, 0), 0)
        items = []
        items.append(Item(label='a', value=2, weight=2))
        items.append(Item(label='b', value=4, weight=2))
        items.append(Item(label='c', value=6, weight=4))
        items.append(Item(label='d', value=9, weight=5))
        total_weight = 8
        expected_value = 13
        result = knapsack.fill_knapsack(items, total_weight)
        assert_equal(result, expected_value)
        print('Success: test_knapsack_top_down')

def main():
    test = TestKnapsack()
    test.test_knapsack_bottom_up()
    test.test_knapsack_top_down()


if __name__ == '__main__':
    main()