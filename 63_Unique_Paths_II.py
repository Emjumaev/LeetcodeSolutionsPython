from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.hashMap = {}
        return self.dfs(obstacleGrid, 0, 0)

    def dfs(self, obstacleGrid: List[List[int]], i: int, j: int) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if i >= m or j >= n:
            return 0

        if obstacleGrid[i][j] == 1:
            return 0

        if i == m - 1 and j == n - 1:
            return 1

        if (i + 1, j) not in self.hashMap:
            self.hashMap[i + 1, j] = self.dfs(obstacleGrid, i + 1, j)

        if (i, j + 1) not in self.hashMap:
            self.hashMap[i, j + 1] = self.dfs(obstacleGrid, i, j + 1)

        return self.hashMap[i + 1, j] + self.hashMap[i, j + 1]
