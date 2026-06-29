# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = None

        for list in lists:
            res = self.mergeList(res, list)

        return res

    def mergeList(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2
        dummy = ListNode(0)
        cur = dummy

        while(cur1 != None and cur2 != None):
            if cur1.val < cur2.val:
                cur.next = ListNode(cur1.val)
                cur1 = cur1.next
            else:
                cur.next = ListNode(cur2.val)
                cur2 = cur2.next

            cur = cur.next

        if cur1 == None:
            cur.next = cur2
        else:
            cur.next = cur1

        return dummy.next
