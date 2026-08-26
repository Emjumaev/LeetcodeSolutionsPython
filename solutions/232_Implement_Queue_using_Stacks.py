class MyQueue:

    def __init__(self):
        self.mainStack = []
        self.secondaryStack = []


    def push(self, x: int) -> None:
        self.mainStack.append(x)

    def pop(self) -> int:
        while(len(self.mainStack) > 1):
            self.secondaryStack.append(self.mainStack.pop())

        popedItem = self.mainStack.pop()

        while(len(self.secondaryStack) > 0):
            self.mainStack.append(self.secondaryStack.pop())

        return popedItem

    def peek(self) -> int:
        lastPopedItem = 0

        while(len(self.mainStack) > 0):
            lastPopedItem = self.mainStack.pop()
            self.secondaryStack.append(lastPopedItem)

        while(len(self.secondaryStack) > 0):
            self.mainStack.append(self.secondaryStack.pop())

        return lastPopedItem

    def empty(self) -> bool:
        return len(self.mainStack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
