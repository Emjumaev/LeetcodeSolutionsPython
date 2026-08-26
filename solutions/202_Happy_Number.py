class Solution:
    def isHappy(self, n: int) -> bool:
        hashSet = set()

        while(n != 1):

            if n in hashSet:
                return False
            else:
                hashSet.add(n)

            n = self.sumDigits(n)

        return True


    def sumDigits(self, n: int) -> int:
        res = 0
        while(n > 0):
            res = res + (n % 10) ** 2
            n = n // 10
        return res
