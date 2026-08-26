class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        res = self.power(x, abs(n))
        
        if n < 0:
            return 1 / res
        else:
            return res
        
    def power(self, x: float, n: int) -> float:
        if n == 1:
            return x
        
        if n == 0:
            return 1
        
        if n % 2 == 0:
            halfPower = self.power(x, n / 2)
            return halfPower * halfPower
        else:
            return x * self.power(x, n - 1)

"""
Time: Log(n)
Space: Log(n)
"""
