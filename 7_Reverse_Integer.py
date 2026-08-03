class Solution:
    def reverse(self, x: int) -> int:
        maxVal = 2 ** 31 - 1
        minVal = -(2 ** 31)
        res = 0
        sign = 1
        
        if x < 0:
            sign = -1
        x = abs(x)
        
        while(x != 0):
            digit = x % 10

            print(digit)

            if res * sign > maxVal // 10 or (res * sign == maxVal // 10 and digit >= 7):
                return 0
            
            if res * sign < minVal // 10 + 1 or (res * sign == minVal // 10 + 1 and digit >= 8):
                return 0
            
            res *= 10
            res += digit
            x = x // 10
        
        return res * sign
