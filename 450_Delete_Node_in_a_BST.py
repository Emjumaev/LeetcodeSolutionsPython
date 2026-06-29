# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return None

        rootVal = root.val

        if key < rootVal:
            root.left = self.deleteNode(root.left, key)
        elif key > rootVal:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            # find smallest on the right subtree
            cur = root.right
            minVal = cur.val
            while(cur != None):
                minVal = min(minVal, cur.val)
                cur = cur.left

            root.val = minVal

            root.right = self.deleteNode(root.right, minVal)

        return root
