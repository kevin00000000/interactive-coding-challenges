from nose.tools import assert_equal
from nose.tools import assert_raises
from nose.tools import assert_true
from enum import Enum
import sys


class Type(Enum):
    SELL = 0
    BUY = 1


class Transaction(object):

    def __init__(self, type, day, price):
        self.type = type
        self.day = day
        self.price = price

    def __eq__(self, other):
        return self.type == other.type and \
            self.day == other.day and \
            self.price == other.price

    def __repr__(self):
        return str(self.type) + ' day: ' + \
            str(self.day) + ' price: ' + \
            str(self.price)


class StockTrader(object):

    def __init__(self):
        self.results = []
        self.result_transactions = []

    def find_max_profit(self, prices, k):
        if prices is None or k is None:
            raise TypeError("param is None")
        if not prices or not k:
            return []
        self._init_result(len(prices), k)
        self._fill_result(prices, k)
        return self.results[len(prices)][k], self.result_transactions[len(prices)][k]

    def _init_result(self, n, k):
        for i in range(n+1):
            self.results.append([])
            self.result_transactions.append([])
            for _ in range(k+1):
                self.results[i].append(0)
                self.result_transactions[i].append([])
    
    def _fill_result(self, prices, k):
        n = len(prices)
        for i in range(n+1):
            for j in range(k+1):
                if not i or not j:
                    self.results[i][j] = 0
                    self.result_transactions[i][j] = []
                    continue
                max_profit = -sys.maxsize
                max_buy = 0
                for m in range(i):
                    temp_profit = prices[i-1] - prices[m] + self.results[m][j-1]
                    if max_profit < temp_profit:
                        max_buy = m
                        max_profit = temp_profit
                self.results[i][j] = max(self.results[i-1][j], max_profit)
                if self.results[i-1][j] >= max_profit:
                    self.results[i][j] = self.results[i-1][j]
                    self.result_transactions[i][j].extend(self.result_transactions[i-1][j])
                else:
                    self.results[i][j] = max_profit
                    self.result_transactions[i][j].extend(self.result_transactions[i-1][j])
                    self.result_transactions[i][j].append(Transaction(Type.BUY, max_buy, prices[max_buy]))
                    self.result_transactions[i][j].append(Transaction(Type.SELL, i-1, prices[i-1]))


class TestMaxProfit(object):

    def test_max_profit(self):
        stock_trader = StockTrader()
        assert_raises(TypeError, stock_trader.find_max_profit, None, None)
        assert_equal(stock_trader.find_max_profit(prices=[], k=0), [])
        prices = [5, 4, 3, 2, 1]
        k = 3
        assert_equal(stock_trader.find_max_profit(prices, k), (0, []))
        prices = [2, 5, 7, 1, 4, 3, 1, 3]
        profit, transactions = stock_trader.find_max_profit(prices, k)
        assert_equal(profit, 10)
        assert_true(Transaction(Type.SELL,
                                day=7,
                                price=3) in transactions)
        assert_true(Transaction(Type.BUY,
                                day=6,
                                price=1) in transactions)
        assert_true(Transaction(Type.SELL,
                                day=4,
                                price=4) in transactions)
        assert_true(Transaction(Type.BUY,
                                day=3,
                                price=1) in transactions)
        assert_true(Transaction(Type.SELL,
                                day=2,
                                price=7) in transactions)
        assert_true(Transaction(Type.BUY,
                                day=0,
                                price=2) in transactions)
        print('Success: test_max_profit')


def main():
    test = TestMaxProfit()
    test.test_max_profit()


if __name__ == '__main__':
    main()