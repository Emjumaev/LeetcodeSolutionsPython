class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        while(x > 0 or y > 0):
            digit1 = x % 2
            digit2 = y % 2
            if digit1 != digit2:
                res += 1
            x = x // 2
            y = y // 2

        return res
