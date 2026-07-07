class Solution:

    alreadyDeleted = False

    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while(left < right):
            if s[left] != s[right]:
                if self.alreadyDeleted == True:
                    return False
                self.alreadyDeleted = True
                return (self.validPalindrome(s[left:right])
                or self.validPalindrome(s[left+1:right+1]))
            left += 1
            right -= 1
        return True
