from nose.tools import assert_equal


class MakeChange(object):

    def __init__(self):
        self.result = {}
    
    def make_change(self, coins, total):
        if coins is None or total is None:
            raise TypeError('invalid param')
        if not coins or not total:
            return 0
        self._init_result(len(coins))
        self._fill_result(coins, len(coins), total)
        return self.result[len(coins)][total]

    def _init_result(self, n):
        for _ in range(n+1):
            self.result[_] = {}

    def _fill_result(self, coins, n, total):
        for i in range(n+1):
            for t in range(total+1):
                if not t:
                    self.result[i][t] = 1
                    continue
                if not i :
                    self.result[i][t] = 0
                    continue
                if coins[i-1] <= t:
                    self.result[i][t] = self.result[i][t-coins[i-1]] + self.result[i-1][t]
                else:
                    self.result[i][t] = self.result[i-1][t]


def change_ways(total, coins):
    return MakeChange().make_change(coins, total)



class Challenge(object):

    def test_coin_change_ways(self,solution):
        assert_equal(solution(0, [1, 2]), 0)
        assert_equal(solution(100, [1, 2, 3]), 884)
        assert_equal(solution(1000, range(1, 101)), 15658181104580771094597751280645)
        print('Success: test_coin_change_ways')


def main():
    test = Challenge()
    test.test_coin_change_ways(change_ways)


if __name__ == '__main__':
    main()