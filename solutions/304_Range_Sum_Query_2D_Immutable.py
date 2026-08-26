class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefixMatrix = []
        self.matrix = matrix

        for arr in matrix:
            curSum = 0
            prefixArr = []
            for num in arr:
                curSum += num
                prefixArr.append(curSum)
            self.prefixMatrix.append(prefixArr)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        totalSum = 0

        for i in range(row1, row2+1):
            prefixArr = self.prefixMatrix[i]
            arr = self.matrix[i]

            prefixSum = prefixArr[col2] - prefixArr[col1] + arr[col1]
            totalSum += prefixSum

        return totalSum



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
