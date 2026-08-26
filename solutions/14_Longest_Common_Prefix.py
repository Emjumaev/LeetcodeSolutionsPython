class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]

        for str in strs:
            res = self.findLCP(res, str)

        return res

    def findLCP(self, str1: str, str2: str) -> str:
        i = 0
        j = 0
        res = ""

        while(i < len(str1) and j < len(str2)):
            if str1[i] != str2[j]:
                return res

            res += str1[i]

            i += 1
            j += 1

        return res
