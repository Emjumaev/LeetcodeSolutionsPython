class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        length = 0

        for char in s:
            if char != " ":
                length += 1
            else:
                if length != 0:
                    res = length
                length = 0

        return length if length != 0 else res
