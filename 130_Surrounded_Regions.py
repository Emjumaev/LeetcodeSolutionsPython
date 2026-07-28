class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.visit = set()

        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == "O" and (i, j) not in self.visit:
                    # perform dfs
                    regions = self.dfs(board, i, j, [])
                    if regions != []:
                        # capture surrounded region
                        for (a, b) in regions:
                            board[a][b] = "X"

    def dfs(self, board, i, j, path):
        rows, cols = len(board), len(board[0])

        self.visit.add((i, j))
        path.append((i, j))

        escaped = i == 0 or i == rows - 1 or j == 0 or j == cols - 1

        for k, l in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            a, b = i + k, j + l

            if not (0 <= a < rows and 0 <= b < cols):
                continue
            if board[a][b] == "X" or (a, b) in self.visit:
                continue

            if self.dfs(board, a, b, path) == []:
                escaped = True          # note: no return

        return [] if escaped else path
