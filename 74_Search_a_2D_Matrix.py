class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rLeft = 0
        rRight = len(matrix) - 1

        while(rLeft <= rRight):
            rMiddle = (rLeft + rRight) // 2

            if target < matrix[rMiddle][0]:
                rRight = rMiddle - 1
            elif target > matrix[rMiddle][len(matrix[0]) - 1]:
                rLeft = rMiddle + 1
            else:
                arr = matrix[rMiddle]

                l = 0
                r = len(arr) - 1
                while(l <= r):
                    m = (l + r) // 2

                    if target > arr[m]:
                        l = m + 1
                    elif target < arr[m]:
                        r = m - 1
                    else:
                        return True

                return False

        return False
