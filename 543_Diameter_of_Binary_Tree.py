# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root)

        return self.res

    def dfs(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        leftVal = self.dfs(root.left)
        rightVal = self.dfs(root.right)
        self.res = max(self.res, leftVal + rightVal)

        return 1 + max(leftVal, rightVal)
