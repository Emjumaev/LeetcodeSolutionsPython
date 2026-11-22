class Solution:
    def toLowerCase(self, s: str) -> str:
        result = ""

        for char in s:
            if 65 <= ord(char) <= 90:
                result += chr(ord(char) + 32)
            else:
                result += char

        return result
