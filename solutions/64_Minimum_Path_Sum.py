class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        self.memo = {}
        return self.dfs(grid, 0, 0)
        
    def dfs(self, grid: list[list[int]], i: int, j: int) -> int:
        
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return grid[i][j]

        if i >= len(grid) or j >= len(grid[0]):
            return float('inf')
        
        if (i + 1, j) not in self.memo:
            self.memo[i + 1, j] = self.dfs(grid, i + 1, j)
        
        if (i, j + 1) not in self.memo:
            self.memo[i, j + 1] = self.dfs(grid, i, j + 1)

        return grid[i][j] + min(self.memo[i + 1, j], self.memo[i, j + 1])
