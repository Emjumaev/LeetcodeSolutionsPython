class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if grid[0][0] == 1:
            return -1
        
        n = len(grid)

        if n == 1:
            return 1

        queue = []
        visited = set()
        level = 1

        queue.append((0, 0))

        while(len(queue) != 0):
            for _ in range(len(queue)):
                drop = queue.pop(0)
                i = drop[0]
                j = drop[1]

                for x, y in [(1, 0), (0, 1), (1, 1), (1, -1), (-1, 0), (0, -1), (-1, -1), (-1, 1)]:
                    if i + x < 0 or i + x >= n or j + y < 0 or j + y >= n:
                        continue

                    if (i + x, j + y) in visited:
                        continue
                    
                    if grid[i + x][j + y] == 1:
                        continue

                    if i + x == n - 1 and j + y == n - 1:
                        return level + 1

                    visited.add((i + x, j + y))
                    queue.append((i + x, j + y))

            level += 1
        
        return -1
