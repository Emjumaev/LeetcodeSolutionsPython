# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        self.dfs(root, float('-inf'))

        return self.res

    def dfs(self, node: TreeNode, maxVal: int):
        if node == None:
            return

        if node.val >= maxVal:
            self.res += 1

        self.dfs(node.left, max(maxVal, node.val))
        self.dfs(node.right, max(maxVal, node.val))
