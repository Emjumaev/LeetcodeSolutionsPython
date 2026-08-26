class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        carry = 1

        for i in range(len(digits)-1, -1, -1):
            print( digits[i])
            sum = digits[i] + carry
            res.append(sum % 10)
            carry = sum // 10

        if carry != 0:
            res.append(carry)

        return res[::-1]
