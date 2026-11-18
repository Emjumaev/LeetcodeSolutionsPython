# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        leftPortion = []
        rightPortion = []

        cur = head
        while(cur):
            if cur.val < x:
                leftPortion.append(cur)
            else:
                rightPortion.append(cur)
            cur = cur.next

        dummy = ListNode(0)
        cur = dummy
        for node in leftPortion:
            cur.next = node
            cur = cur.next

        for node in rightPortion:
            cur.next = node
            cur = cur.next

        cur.next = None
        return dummy.next
