# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        root = self.insert(root, val)

        return root

    def insert(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if root == None:
            return TreeNode(val)

        rootVal = root.val
        if val < rootVal:
            root.left = self.insert(root.left, val)
        elif val > rootVal:
            root.right = self.insert(root.right, val)

        return root
