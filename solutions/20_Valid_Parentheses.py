class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {"]": "[", "}": "{", ")": "("}
        stack = []

        for char in s:
            if char in hashMap:
                if len(stack) == 0:
                    return False

                lastChar = stack[-1]
                if lastChar == hashMap[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0
