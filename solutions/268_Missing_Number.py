class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hashSet = set()
        for num in nums:
            hashSet.add(num)

        for i in range(len(nums)+1):
            if i not in hashSet:
                return i

        return -1
