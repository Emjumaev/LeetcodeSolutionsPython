class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        lastRow = [1, 1]
        while(rowIndex >= 2):
            newRow = []

            newRow.append(1)
            for i in range(len(lastRow) - 1):
                newRow.append(lastRow[i] + lastRow[i + 1])
            newRow.append(1)

            lastRow = newRow
            rowIndex -= 1

        return lastRow

"""
Time: 1 + 2 + 3 + ... + n = (n + 1) / 2 * n = O(n^2)
Space: O(n) for the current and previous rows.
"""
