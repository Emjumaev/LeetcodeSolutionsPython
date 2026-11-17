class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        res = 0
        multiplier = 1

        for num in nums:
            res += multiplier * num
            multiplier *= -1

        return res
