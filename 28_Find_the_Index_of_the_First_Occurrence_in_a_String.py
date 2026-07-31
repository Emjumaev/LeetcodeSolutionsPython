class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        for i in range(len(haystack)):
            l, r = i, 0
            while(l < len(haystack) and r < len(needle)):
                if haystack[l] == needle[r]:
                    if r == len(needle) - 1:
                        return i
                else:
                    break
                l += 1
                r += 1

        return -1
