class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        res = []
        for c in range(len(matrix[0])):
            arr = []
            for r in range(len(matrix)):
                arr.append(matrix[r][c])
            res.append(arr)

        return res
