# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        self.minHeight = float('inf')
        self.dfs(root, 1)
        return self.minHeight

    def dfs(self, root: Optional[TreeNode], height: int):
        if root == None:
            return

        if root.left == None and root.right == None:
            self.minHeight = min(self.minHeight, height)
            return

        self.dfs(root.left, height + 1)
        self.dfs(root.right, height + 1)
