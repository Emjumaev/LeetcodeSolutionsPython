class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        cur = self.head
        i = 0

        while cur:
            if i == index:
                return cur.val
            i += 1
            cur = cur.next

        return -1

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        if self.head:
            newNode.next = self.head
            self.head = newNode
        else:
            self.head = newNode
            self.tail = newNode

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        if self.tail:
            self.tail.next = newNode
            self.tail = newNode
        else:
            self.head = newNode
            self.tail = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        prev = None
        cur = self.head
        i = 0

        if index == 0:
            self.addAtHead(val)
            return

        while cur:
            if i == index:
                newNode = Node(val)
                prev.next = newNode
                newNode.next = cur
                return
            prev = cur
            cur = cur.next
            i += 1

        if i == index:
            self.addAtTail(val)

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head
        prev = None
        i = 0

        if index == 0:
            self.head = self.head.next

            if self.head is None:
                self.tail = None
            return

        while cur:
            if i == index:
                prev.next = cur.next
                if cur.next is None:
                    self.tail = prev
                return
            prev = cur
            cur = cur.next
            i += 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
