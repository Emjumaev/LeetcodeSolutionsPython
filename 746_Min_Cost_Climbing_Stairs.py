class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.memo = {}

        return min(self.climb(cost, 0), self.climb(cost, 1))

    def climb(self, cost: List[int], i: int) -> int:
        if i >= len(cost):
            return 0

        if i not in self.memo:
            self.memo[i] = cost[i] + min(self.climb(cost, i + 1), self.climb(cost, i + 2))

        return self.memo[i]
