from nose.tools import assert_equal, assert_raises
import sys


class CoinChanger(object):
    def __init__(self):
        self.result = {}

    def make_change(self, coins, total):
        if coins is None or total is None:
            raise TypeError('coins or total is None')
        if not len(coins) or not total:
            return 0
        self._init_result(len(coins), total)
        self._fill_result(coins, len(coins), total)
        return self.result[len(coins)][total]
    
    def _init_result(self, n, total):
        for _ in range(0, n+1):
            self.result[_] = {}
    
    def _fill_result(self, coins, n, total):
        for i in range(n+1):
            for t in range(total+1):
                if not t:
                    self.result[i][t] = 0
                    continue
                if not i:
                    self.result[i][t] = sys.maxsize
                    continue
                if coins[i-1] <= t:
                    self.result[i][t] = min(self.result[i-1][t], self.result[i][t-coins[i-1]] + 1)
                else:
                    self.result[i][t] = self.result[i-1][t]

class TestCoinChange(object):

    def test_coin_change(self):
        coin_changer = CoinChanger()
        assert_raises(TypeError, coin_changer.make_change, None, None)
        assert_equal(coin_changer.make_change([], 0), 0)
        assert_equal(coin_changer.make_change([1, 2, 3], 5), 2)
        assert_equal(coin_changer.make_change([3, 2, 1], 5), 2)
        assert_equal(coin_changer.make_change([3, 2, 1], 8), 3)
        print('Success: test_coin_change')


def main():
    test = TestCoinChange()
    test.test_coin_change()


if __name__ == '__main__':
    main()