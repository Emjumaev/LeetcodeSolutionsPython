class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for index, val in enumerate(nums):
            if index == self.sumOfDigits(val):
                return index

        return -1

    def sumOfDigits(self, num: int) -> int:
        res = 0
        while(num > 0):
            res += num % 10
            num = num // 10

        return res
