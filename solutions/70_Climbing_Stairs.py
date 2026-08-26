class Solution:

    hashMap = {}

    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        res = 0

        if n - 1 not in self.hashMap:
            self.hashMap[n - 1] = self.climbStairs(n - 1)

        if n - 2 not in self.hashMap:
            self.hashMap[n - 2] = self.climbStairs(n - 2)


        return self.hashMap[n - 1] + self.hashMap[n - 2]
