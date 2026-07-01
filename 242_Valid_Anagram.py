class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap1 = {}
        hashMap2 = {}

        for char in s:
            if char in hashMap1:
                hashMap1[char] += 1
            else:
                hashMap1[char] = 1

        for char in t:
            if char in hashMap2:
                hashMap2[char] += 1
            else:
                hashMap2[char] = 1

        return hashMap1 == hashMap2
