# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:
        sortedArr = []

        cur = head
        while(cur):
            sortedArr.append(cur.val)
            cur = cur.next

        return self.constructBST(sortedArr)

    def constructBST(self, arr: [int]) -> TreeNode | None:
        if len(arr) == 0:
            return None

        if len(arr) == 1:
            return TreeNode(arr[0])

        node = TreeNode(arr[len(arr) // 2])
        node.left = self.constructBST(arr[:len(arr) // 2])
        node.right = self.constructBST(arr[(len(arr) // 2 + 1):])

        return node
