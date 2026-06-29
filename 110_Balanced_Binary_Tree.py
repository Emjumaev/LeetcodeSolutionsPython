# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True

        self.dfs(root)

        return self.res

    def dfs(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1

        leftHeight = self.dfs(root.left)
        rightHeight = self.dfs(root.right)

        if abs(leftHeight - rightHeight) > 1:
            self.res = False

        return max(leftHeight, rightHeight) + 1
