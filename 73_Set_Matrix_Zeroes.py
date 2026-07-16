class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i = len(matrix) - 1
        rowSet = set()
        colSet = set()

        while(i >= 0):
            j = len(matrix[0]) - 1
            while(j >= 0):
                if matrix[i][j] == 0:
                    rowSet.add(i)
                    colSet.add(j)
                j -= 1
            i -= 1

        for r in rowSet:
            for j in range(len(matrix[0])):
                matrix[r][j] = 0

        for c in colSet:
            for i in range(len(matrix)):
                matrix[i][c] = 0
