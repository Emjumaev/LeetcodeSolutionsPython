class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.combinations = []

        self.dfs(candidates, target, [], 0, 0)

        return self.combinations
    
    def dfs(self, candidates: List[int], target: int, path: [Int], sum: int, start: int):
        if sum > target:
            return
        
        if sum == target:
            self.combinations.append(path)
            return
        
        for i in range(start, len(candidates)):
            candidate = candidates[i]
            newPath = path.copy()
            newPath.append(candidate)
            self.dfs(candidates, target, newPath, sum + candidate, i)
