class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProduct = []
        rightProduct = []
        cur = 1
        for num in nums:
            cur *= num
            leftProduct.append(cur)

        cur = 1
        for num in nums[::-1]:
            cur *= num
            rightProduct.append(cur)
        rightProduct = rightProduct[::-1]

        res = []
        for (ind, val) in enumerate(nums):
            if ind == 0:
                res.append(rightProduct[ind + 1])
            elif ind == len(nums) - 1:
                res.append(leftProduct[ind - 1])
            else:
                res.append(leftProduct[ind - 1] * rightProduct[ind + 1])

        return res
