class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left, right, res = 0, 0, 0
        hash_map = {}

        for right in range(len(s)):
            char = s[right]

            if char in hash_map:
                while(hash_map[char] >= 2):
                        hash_map[s[left]] -= 1
                        left += 1
                hash_map[char] += 1
            else:
                hash_map[char] = 1
            
            res = max(res, right - left + 1)       

        return res 
