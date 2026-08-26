class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while(left < right):
            if self.isValidChar(s[left]) == False:
                left += 1
                continue

            if self.isValidChar(s[right]) == False:
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

    def isValidChar(self, char: str) -> bool:
        asciiVal = ord(char)

        if asciiVal >= 65 and asciiVal <= 90:
            return True

        if asciiVal >= 97 and asciiVal <= 122:
            return True

        if asciiVal >= 48 and asciiVal <= 57:
            return True

        return False
