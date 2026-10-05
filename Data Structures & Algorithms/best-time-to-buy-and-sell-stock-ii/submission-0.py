class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i, price in enumerate(prices):
            if i == len(prices) - 1:
                return profit
            if prices[i] < prices[i + 1]:
                profit += prices[i + 1] - prices[i]
