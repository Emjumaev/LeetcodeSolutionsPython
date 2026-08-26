# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.dfs(root, targetSum, 0)
    
    def dfs(self, root: Optional[TreeNode], targetSum: int, currentSum: int) -> bool:

        if root == None:
            return False

        if root.left == None and root.right == None:
            if currentSum + root.val == targetSum:
                return True
        
        if self.dfs(root.left, targetSum, currentSum + root.val):
            return True

        if self.dfs(root.right, targetSum, currentSum + root.val):
            return True
        
        return False
