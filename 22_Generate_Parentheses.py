class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.count = n
        self.generate(0, "", [])

        return self.res

    def generate(self, openingCount: int, path: str, stack: List[str]):
        if len(path) == self.count * 2:
            self.res.append(path)

        if openingCount < self.count:
            path += "("
            stack.append("(")
            openingCount += 1
            self.generate(openingCount, path, stack)
            openingCount -= 1
            path = path[:-1]
            stack.pop()

        if len(stack) != 0:
            path += ")"
            stack.pop()
            self.generate(openingCount, path, stack)
            path = path[:-1]
            stack.append("(")
