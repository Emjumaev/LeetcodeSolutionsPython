class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        counter = Counter(s)
        containsOdd = False

        for i, v in counter.items():
            res += v // 2 * 2

            if v % 2 == 1:
                containsOdd = True

        return res + 1 if containsOdd else res
