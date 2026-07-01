class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        dummy1 = Node(0, 0)
        dummy2 = Node(0, 0)
        dummy1.next = dummy2
        dummy2.prev = dummy1
        self.head = dummy1
        self.tail = dummy2
        self.hashMap = {}

    def get(self, key: int) -> int:
        if key not in self.hashMap:
            return -1
        # remove the key from linked list
        nodeToRemove = self.hashMap[key]
        nodeToRemove.prev.next = nodeToRemove.next
        nodeToRemove.next.prev = nodeToRemove.prev

        # add it to the back
        backNode = self.tail.prev
        backNode.next = nodeToRemove
        nodeToRemove.prev = backNode
        nodeToRemove.next = self.tail
        self.tail.prev = nodeToRemove

        return nodeToRemove.val

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            self.hashMap[key].val = value
            self.get(key)
            return

        newNode = Node(key, value)
        self.hashMap[key] = newNode

        if self.capacity == 0:
            firstKey = self.head.next.key
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
            self.hashMap.pop(firstKey)

            self.capacity += 1

        backNode = self.tail.prev
        backNode.next = newNode
        newNode.prev = backNode
        newNode.next = self.tail
        self.tail.prev = newNode

        self.capacity -= 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
