from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []
        res.append(-1)
        curMax = -1

        for i in range(len(arr) - 1, 0, -1):
            if arr[i] > curMax:
                curMax = arr[i]
            res.append(curMax)

        return res[::-1]
