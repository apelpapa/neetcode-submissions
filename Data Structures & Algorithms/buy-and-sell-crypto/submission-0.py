class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        last_max = 0

        for i, price in enumerate(prices):
            if i == len(prices) - 1:
                return last_max
            if max(prices[i+1:]) - price > last_max:
                last_max = max(prices[i+1:]) - price