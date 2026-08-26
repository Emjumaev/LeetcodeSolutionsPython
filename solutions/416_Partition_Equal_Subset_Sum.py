class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        self.totalSum = sum(nums)
        self.memo = {}

        if self.totalSum % 2 == 1:
            return False

        return self.dfs(nums, 0, 0)

    def dfs(self, nums: List[int], ind: int, curSum: int) -> bool:
        target = self.totalSum // 2
        key = (ind, curSum)

        if key in self.memo:
            return self.memo[key]

        if curSum == target:
            return True
        if ind == len(nums) or curSum > target:
            return False

        res = (
            self.dfs(nums, ind + 1, curSum + nums[ind]) or
            self.dfs(nums, ind + 1, curSum)
        )

        self.memo[key] = res
        return res
