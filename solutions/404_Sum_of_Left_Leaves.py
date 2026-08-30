# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        self.dfs(root)

        return self.sum

    def dfs(self, root: Optional[TreeNode]):
        if root == None:
            return

        if root.left != None and root.left.left == None and root.left.right == None:
            self.sum += root.left.val

        self.dfs(root.left)
        self.dfs(root.right)
