class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        paths = [[]]

        for num in nums:
            for i in range(len(paths)):
                newPath = paths[i].copy()
                newPath.append(num)
                paths.append(newPath)
        
        return paths
