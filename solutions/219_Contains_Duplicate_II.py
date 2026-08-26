class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashSet = set()

        if k >= len(nums):
            k = len(nums)

        for i in range(k):
            if nums[i] in hashSet:
                return True
            else:
                hashSet.add(nums[i])

        l = 0
        r = k
        while(r < len(nums)):
            if nums[r] in hashSet:
                return True
            else:
                hashSet.add(nums[r])

            hashSet.remove(nums[l])

            l += 1
            r += 1

        return False
