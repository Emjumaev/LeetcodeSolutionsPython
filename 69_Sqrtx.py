class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        l = 1
        r = x
        res = 1

        while(l <= r):
            m = (l + r) // 2

            if m * m < x:
                res = max(res, m)
                l = m + 1
            elif m * m > x:
                r = m - 1
            else:
                return m

        return res
