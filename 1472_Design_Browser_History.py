class Node:
    val = ""
    next = None
    prev = None

    def __init__(self, val: str):
        self.val = val

class BrowserHistory:

    cur = None

    def __init__(self, homepage: str):
        newNode = Node(homepage)
        self.cur = newNode

    def visit(self, url: str) -> None:
        newNode = Node(url)
        self.cur.next = newNode
        newNode.prev = self.cur
        self.cur = newNode

    def back(self, steps: int) -> str:
        i = 0
        while(i < steps):
            if self.cur.prev == None:
                return self.cur.val
            self.cur = self.cur.prev
            i += 1
        return self.cur.val

    def forward(self, steps: int) -> str:
        i = 0
        while(i < steps):
            if self.cur.next == None:
                return self.cur.val
            self.cur = self.cur.next
            i += 1
        return self.cur.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
