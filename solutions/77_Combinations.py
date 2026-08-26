class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.k = k
        self.res = []

        nums = []
        for i in range(1, n + 1):
            nums.append(i)

        self.dfs(nums, -1, [])

        return self.res


    def dfs(self, nums: List[int], ind: int, combination: List[int]):
        if len(combination) == self.k:
            self.res.append(combination)
            return

        for i in range(ind + 1, len(nums)):
            newCombination = combination.copy()
            newCombination.append(nums[i])
            self.dfs(nums, i, newCombination)
