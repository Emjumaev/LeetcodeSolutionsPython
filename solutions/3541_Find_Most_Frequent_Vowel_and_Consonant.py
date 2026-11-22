class Solution:
    def maxFreqSum(self, s: str) -> int:
        hash_map = {}

        for char in s:
            if char in hash_map:
                hash_map[char] += 1
            else:
                hash_map[char] = 1

        max1 = 0
        max2 = 0
        for key, val in hash_map.items():
            if key in {"a", "e", "i", "o", "u"}:
                max1 = max(max1, val)
            else:
                max2 = max(max2, val)

        return max1 + max2
