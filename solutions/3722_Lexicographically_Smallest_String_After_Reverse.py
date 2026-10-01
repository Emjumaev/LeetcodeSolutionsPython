class Solution:
    def lexSmallest(self, s: str) -> str:
        if len(s) == 1:
            return s
            
        strings = []

        for i in range(len(s)):
            left = s[:i + 1]
            right = s[i + 1:]
            strings.append(left[::-1] + right)
            strings.append(left + right[::-1])

        strings.sort()

        return strings[0]
