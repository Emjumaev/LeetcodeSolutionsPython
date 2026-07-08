class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.hashMap = {}
        return self.dfs(m, n, 0, 0)

    def dfs(self, m: int, n: int, i: int, j: int) -> int:
        if i >= m or j >= n:
            return 0

        if i == m - 1 and j == n - 1:
            return 1

        if (i + 1, j) not in self.hashMap:
            self.hashMap[i + 1, j] = self.dfs(m, n, i + 1, j)

        if (i, j + 1) not in self.hashMap:
            self.hashMap[i, j + 1] = self.dfs(m, n, i, j + 1)

        return self.hashMap[i + 1, j] + self.hashMap[i, j + 1]
