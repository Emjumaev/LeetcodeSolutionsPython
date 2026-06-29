class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        hashMap = {}

        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        res = []

        for i in range(0, 3):
            if i not in hashMap:
                continue

            count = hashMap[i]
            while(count != 0):
                res.append(i)
                count -= 1

        nums[:] = res
