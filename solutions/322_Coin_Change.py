class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.hashMap = {}

        ans = self.dfs(coins, amount)
        return -1 if ans == float('inf') else ans

    def dfs(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0

        if amount < 0:
            return float('inf')

        res = float('inf')

        for coin in coins:
            if amount - coin not in self.hashMap:
                self.hashMap[amount - coin] = self.dfs(coins, amount - coin)
            res = min(res, 1 + self.hashMap[amount - coin])

        return res
