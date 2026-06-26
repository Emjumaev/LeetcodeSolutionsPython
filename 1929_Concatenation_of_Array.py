from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(0, n, 1):
            nums.append(nums[i])

        return nums
