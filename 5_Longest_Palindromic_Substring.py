class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        res = s[0]

        for i in range(len(s)):
            l, r = i, i
            curLen = 1

            while(l >= 0 and r < len(s) and s[l] == s[r]):
                curLen += 2
                if curLen > maxLen:
                    maxLen = curLen
                    res = s[l:r+1]
                l -= 1
                r += 1

            l, r = i, i + 1
            curLen = 2

            while(l >= 0 and r < len(s) and s[l] == s[r]):
                curLen += 2
                if curLen > maxLen:
                    maxLen = curLen
                    res = s[l:r+1]
                l -= 1
                r += 1

        return res
