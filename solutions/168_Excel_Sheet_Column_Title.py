class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""

        while(columnNumber > 26):
            mod = columnNumber % 26
            # map it to the character
            if mod == 0:
                char = "Z"
                columnNumber = columnNumber // 26 - 1
            else:
                char = chr(mod + 64)
                columnNumber = columnNumber // 26

            res = char + res

        # map it to the character
        res = chr(columnNumber + 64) + res

        return res
