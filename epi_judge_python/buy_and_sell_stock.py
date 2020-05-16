from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    best_price_so_far, max_profit_so_far = prices[0], 0.0 
    for i in range(1, len(prices)):
        max_profit_so_far = max(max_profit_so_far, prices[i] - best_price_so_far)
        best_price_so_far = min(best_price_so_far, prices[i])
    return max_profit_so_far


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
