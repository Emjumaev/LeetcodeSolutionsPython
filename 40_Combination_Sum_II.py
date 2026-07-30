class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.res = []

        for i in range(len(candidates)):
            if i > 0 and candidates[i] == candidates[i - 1]:
                continue
            self.dfs(candidates, i, target - candidates[i], [candidates[i]])

        return self.res

    def dfs(self, candidates: List[int], i: int, target: int, path: List[int]):

        if target == 0:
            self.res.append(path.copy())
            return
        elif target < 0:
            return

        for j in range(i + 1, len(candidates)):
            if j > i + 1 and candidates[j] == candidates[j - 1]:
                continue
            path.append(candidates[j])
            self.dfs(candidates, j, target - candidates[j], path)
            path.pop()
