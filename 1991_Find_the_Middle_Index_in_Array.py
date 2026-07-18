class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = sum(nums)

        for (ind, val) in enumerate(nums):
            rightSum -= val
            if leftSum == rightSum:
                return ind
            leftSum += val

        return -1
