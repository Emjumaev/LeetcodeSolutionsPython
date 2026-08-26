class Solution:
    def numDecodings(self, s: str) -> int:
        self.memo = {}

        return self.decode(s, -1)

    def decode(self, s: str, i: int) -> int:
        if i == len(s) - 1:
            return 1

        if i + 1 >= len(s):
            num1 = 0
        else:
            num1 = int(s[i + 1])

        if i + 2 >= len(s):
            num2 = 0
        else:
            num2 = int(s[(i + 1):(i + 3)])

        count = 0

        if num1 < 1 or num1 > 26:
            return 0

        if num1 >= 1 and num1 <= 26:
            if i + 1 not in self.memo:
                self.memo[i + 1] = self.decode(s, i + 1)
            count += self.memo[i + 1]

        if num2 >= 1 and num2 <= 26:
            if i + 2 not in self.memo:
                self.memo[i + 2] = self.decode(s, i + 2)
            count += self.memo[i + 2]

        return count
