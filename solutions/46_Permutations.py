class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.dfs(nums, [], set())
        return self.res

    def dfs(self, nums, path, pathSet):
        if len(path) == len(nums):
            self.res.append(path.copy())
            return

        for num in nums:
            if num in pathSet:
                continue

            path.append(num)
            pathSet.add(num)

            self.dfs(nums, path, pathSet)

            path.pop()
            pathSet.remove(num)
