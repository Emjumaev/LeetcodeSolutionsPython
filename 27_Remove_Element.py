from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] == val:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                right -= 1
            else:
                left += 1

        return left
