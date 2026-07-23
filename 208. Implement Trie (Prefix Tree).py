class PrefixTreeNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = PrefixTreeNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for ind, char in enumerate(word):

            if char not in cur.children:
                cur.children[char] = PrefixTreeNode()
            cur = cur.children[char]

            if ind == len(word) - 1:
                cur.isEndOfWord = True
            

    def search(self, word: str) -> bool:
        cur = self.root

        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]

        return cur.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        
        return True
