# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    res = None

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        self.reverse(head)

        return self.res

    def reverse(self, head: Optional[ListNode]):
        if head == None:
            return
        if head.next == None:
            self.res = head
            return

        self.reverseList(head.next)
        head.next.next = head
        head.next = None
