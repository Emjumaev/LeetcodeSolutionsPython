class Solution:
    def decodeMessage(self, key: str, message: str) -> str:

        # building the hashmap O(1)
        hash_map = {}
        cur = 97

        for k in key:
            if cur > 122:
                break

            if k == " ":
                continue

            if k not in hash_map:
                hash_map[k] = chr(cur)
                cur += 1

        # parsing O(n)
        res = ""
        for char in message:
            if char == " ":
                res += " "
            else:
                res += hash_map[char]

        return res
