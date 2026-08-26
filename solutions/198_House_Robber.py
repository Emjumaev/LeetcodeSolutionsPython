from typing import List


class Solution:

    def rob(self, nums: List[int]) -> int:
        self.hashMap = {}
        return self.robHouse(nums, -2)

    def robHouse(self, nums: List[int], index: int) -> int:
        if index >= len(nums):
            return 0

        sum = 0
        if index >= 0:
            sum = nums[index]

        if index+2 not in self.hashMap:
            self.hashMap[index+2] = self.robHouse(nums, index + 2)

        if index+3 not in self.hashMap:
            self.hashMap[index+3] = self.robHouse(nums, index + 3)

        return sum + max(self.hashMap[index+2], self.hashMap[index+3])
