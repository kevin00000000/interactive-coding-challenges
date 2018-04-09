from nose.tools import assert_equal


class CoinChanger(object):

    def __init__(self):
        self.result = {}

    def make_change(self, coins, total):
        if coins is None or total is None:
            return 0
        if not total:
            return 0
        if not coins:
            return 0
        self._init_result(len(coins))
        self._make_change(coins, len(coins), total)
        return self.result[len(coins)][total]
    
    def _init_result(self, n):
        for _ in range(0, n+1):
            self.result[_] = {}

    def _make_change(self, coins, n, total):
        for i in range(0, n+1):
            for t in range(0, total+1):
                if t == 0:
                    self.result[i][t] = 1
                    continue
                if i == 0:
                    self.result[i][t] = 0
                    continue
                if coins[i-1] <= t:
                    self.result[i][t] = self.result[i][t-coins[i-1]] + self.result[i-1][t]
                else:
                    self.result[i][t] = self.result[i-1][t]
        return

        


class Challenge(object):

    def test_coin_change(self):
        coin_changer = CoinChanger()
        assert_equal(coin_changer.make_change([1, 2], 0), 0)
        assert_equal(coin_changer.make_change([1, 2, 3], 5), 5)
        assert_equal(coin_changer.make_change([1, 5, 25, 50], 10), 3)
        print('Success: test_coin_change')


def main():
    test = Challenge()
    test.test_coin_change()


if __name__ == '__main__':
    main()