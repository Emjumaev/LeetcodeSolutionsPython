class PrefixTreeNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = PrefixTreeNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for ind, char in enumerate(word):

            if char not in cur.children:
                cur.children[char] = PrefixTreeNode()
            cur = cur.children[char]

            if ind == len(word) - 1:
                cur.isEndOfWord = True

    def search(self, word: str) -> bool:
        return self.searchForNode(self.root, word)
    
    def searchForNode(self, cur: PrefixTreeNode, word: str) -> bool:

        for ind, char in enumerate(word):
            if char == ".":
                for child in cur.children.values():
                    if self.searchForNode(child, word[(ind + 1):]):
                        return True
                return False
                 
            if char not in cur.children:
                return False
            cur = cur.children[char]

        return cur.isEndOfWord

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
