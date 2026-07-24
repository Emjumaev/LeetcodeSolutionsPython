class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)

        self.memo = {}
        best = self.dfs(nums, 0, set())
        self.memo = {}
        return max(best, self.dfs(nums, 1, set()), self.dfs(nums, 2, set()))

    def dfs(self, nums: List[int], ind: int, path: set[int]) -> int:
        if ind >= len(nums):
            return 0

        if ind == len(nums) - 1 and 0 in path:
            return 0

        path.add(ind)

        if ind + 2 not in self.memo:
            self.memo[ind + 2] = self.dfs(nums, ind + 2, path)

        if ind + 3 not in self.memo:
            self.memo[ind + 3] = self.dfs(nums, ind + 3, path)

        path.remove(ind)
        return nums[ind] + max(self.memo[ind + 2], self.memo[ind + 3])
