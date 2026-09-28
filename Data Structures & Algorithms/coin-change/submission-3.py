class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [amount + 1] * (amount + 1)
        arr[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue
                arr[i] = min(arr[i], arr[i - coin] + 1)
        
        if arr[amount] <= amount:
            return arr[amount]
        return -1