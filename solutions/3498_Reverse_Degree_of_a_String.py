class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0

        for index, char in enumerate(s):
            val = ord(char) - 96
            reverse_val = 27 - val

            res += (index + 1) * reverse_val

        return res
