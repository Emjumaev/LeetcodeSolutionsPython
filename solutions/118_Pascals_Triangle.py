class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []

        if numRows >= 1:
            ans.append([1])

        if numRows >= 2:
            ans.append([1, 1])

        lastRow = [1, 1]
        while(numRows >= 3):
            newRow = []

            newRow.append(1)
            for i in range(len(lastRow) - 1):
                newRow.append(lastRow[i] + lastRow[i + 1])
            newRow.append(1)

            ans.append(newRow)
            lastRow = newRow
            numRows -= 1

        return ans

"""
Time & Space: 1 + 2 + 3 + ... + n = (n + 1) / 2 * n = O(n^2)
"""
