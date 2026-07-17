# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        cur = head.next

        while(cur != None):
            num1 = prev.val
            num2 = cur.val
            gcdNum = self.gcd(num1, num2)
            newNode = ListNode(gcdNum)

            prev.next = newNode
            newNode.next = cur
            prev = cur
            cur = cur.next

        return head

    def gcd(self, num1: int, num2: int) -> int:
        while(num2 != 0):
            temp = num2
            num2 = num1 % num2
            num1 = temp

        return num1
