class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        l, r = 0, 1
        res = 0

        while(r < len(values)):
            res = max(res, values[l] + values[r] + l - r)

            if values[l] + l <= values[r] + r:
                l = r
            r += 1

        return res


"""
Time: O(n)
Space: O(1)
"""
