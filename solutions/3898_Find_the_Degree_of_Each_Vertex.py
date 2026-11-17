class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        res = []
        for arr in matrix:
            count = 0
            for i in arr:
                if i == 1:
                    count += 1

            res.append(count)

        return res
