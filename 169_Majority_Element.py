class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        for (key, value) in counter.items():
            if value > len(nums) / 2:
                return key

        return 0
