class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))

        while(len(queue) != 0):
            for _ in range(len(queue)):
                pop = queue.pop(0)

                i = pop[0]
                j = pop[1]

                for x, y in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
                    if i + x < 0 or i + x >= len(grid) or j + y < 0 or j + y >= len(grid[0]):
                        continue
                    if grid[i + x][j + y] == 0:
                        continue
                    if grid[i + x][j + y] == 2:
                        continue

                    grid[i + x][j + y] = 2
                    queue.append((i + x, j + y))

            res += 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return 0 if res == 0 else res - 1
