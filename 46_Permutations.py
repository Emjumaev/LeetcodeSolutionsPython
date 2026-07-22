class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.dfs(nums, [], set())
        return self.res

    def dfs(self, nums: List[int], path: List[int], pathSet: set[int]):
        if len(path) == len(nums):
            self.res.append(path)
            return

        for num in nums:
            if num not in pathSet:
                newPath = path.copy()
                newPath.append(num)
                newPathSet = pathSet.copy()
                newPathSet.add(num)
                self.dfs(nums, newPath, newPathSet)
