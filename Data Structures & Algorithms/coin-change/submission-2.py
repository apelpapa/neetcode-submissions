class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coin_memo = [amount + 1] * (amount + 1)
        coin_memo[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if i - coin < 0:
                    continue
                coin_memo[i] = min(coin_memo[i], coin_memo[i - coin] + 1)
        
        if coin_memo[amount] <= amount:
            return coin_memo[amount]
        return -1