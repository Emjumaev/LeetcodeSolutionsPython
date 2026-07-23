class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        res = 0
        for num in nums:
            if (num - 1) not in hashSet:
                length = 1
                cur = num + 1
                while(cur in hashSet):
                    hashSet.remove(cur)
                    length += 1
                    cur += 1
                res = max(res, length)

        return res
