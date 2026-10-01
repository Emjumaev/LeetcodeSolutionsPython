class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) % 3 != 0:
            return False
        
        for char in s:
            if len(stack) >= 2 and char == "c" and stack[-1] == "b" and stack[-2] == "a":
                stack.pop()
                stack.pop()
            else:
                stack.append(char)
                
        return len(stack) == 0
