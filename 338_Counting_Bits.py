class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(0, n + 1):
            res.append(self.hammingWeight(i))

        return res

    def hammingWeight(self, n: int) -> int:
        count = 0

        while(n != 0):
            if n % 2 == 1:
                count += 1
            n //= 2

        return count
