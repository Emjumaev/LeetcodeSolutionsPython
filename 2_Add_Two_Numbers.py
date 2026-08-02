# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        carry = 0
        dummy = ListNode(0)
        cur = dummy

        while(cur1 != None or cur2 != None):
            val1 = 0
            if cur1 != None:
                val1 = cur1.val
                cur1 = cur1.next

            val2 = 0
            if cur2 != None:
                val2 = cur2.val
                cur2 = cur2.next

            sum = carry + val1 + val2
            val = sum % 10
            carry = sum // 10

            cur.next = ListNode(val)
            cur = cur.next

        if carry == 1:
            cur.next = ListNode(1)

        return dummy.next
