class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.hashMap = {}
        return self.findCS(text1, text2, 0, 0)

    def findCS(self, text1: str, text2: str, i: int, j: int) -> int:
        if i >= len(text1) or j >= len(text2):
            return 0

        if text1[i] == text2[j]:
            if (i + 1, j + 1) not in self.hashMap:
                self.hashMap[(i + 1, j + 1)] = self.findCS(text1, text2, i + 1, j + 1)
            return 1 + self.hashMap[(i + 1, j + 1)]

        if (i + 1, j) not in self.hashMap:
            self.hashMap[(i + 1, j)] = self.findCS(text1, text2, i + 1, j)

        if (i, j + 1) not in self.hashMap:
            self.hashMap[(i, j + 1)] = self.findCS(text1, text2, i, j + 1)
        return max(self.hashMap[(i + 1, j)], self.hashMap[(i, j + 1)])
