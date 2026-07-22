class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = []

        self.dfs(nums, [], 0)

        return self.res

    def dfs(self, nums: List[int], subset: List[int], ind: int):
        if ind >= len(nums):
            self.res.append(subset.copy())
            return

        subset.append(nums[ind])
        self.dfs(nums, subset, ind + 1)
        subset.remove(nums[ind])

        while(ind + 1 < len(nums) and nums[ind] == nums[ind + 1]):
            ind += 1

        self.dfs(nums, subset, ind + 1)
