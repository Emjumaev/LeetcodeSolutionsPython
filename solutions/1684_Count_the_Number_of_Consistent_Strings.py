class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        self.allowed_set = set(allowed)
        res = 0

        for word in words:
            if self.isConsistent(word):
                res += 1
        
        return res

    def isConsistent(self, word: str) -> bool:
        for char in word:
            if char not in self.allowed_set:
                return False
        
        return True
