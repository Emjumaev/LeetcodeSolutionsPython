class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        for p in range(len(nums)):
            if p != 0 and nums[p] == nums[p - 1]:
                continue

            left = p + 1
            right = len(nums) - 1
            target = -nums[p]

            while(left < right):
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    res.append([nums[left], nums[right], nums[p]])
                    left += 1
                    right -= 1

                    while(nums[left] == nums[left - 1] and left < right):
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return res
