class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:

        leftSums = []
        rightSums = []
        res = []

        left = 0
        leftSum = 0
        rightSum = 0

        while(left < len(nums)):
            leftSums.append(leftSum)
            rightSums.append(rightSum)

            right = len(nums) - left - 1
            leftSum += nums[left]
            rightSum += nums[right]

            left += 1
        
        rightSums.reverse()

        for i in range(len(leftSums)):
            res.append(abs(leftSums[i] - rightSums[i]))

        return res
