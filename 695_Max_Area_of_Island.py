class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(res, self.dfs(grid, i, j))
        
        return res

    def dfs(self, grid: List[List[str]], r: int, c: int) -> int:
        res = 0

        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            return res

        if grid[r][c] == 0:
            return res

        res += 1
        grid[r][c] = 0

        res += self.dfs(grid, r + 1, c)
        res += self.dfs(grid, r - 1, c)
        res += self.dfs(grid, r, c + 1)
        res += self.dfs(grid, r, c - 1)

        return res
