# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode | None) -> int:
        self.sum = 0
        self.dfs(root, None, None)

        return self.sum

    def dfs(self, root: TreeNode | None, parent: TreeNode | None, grandparent: TreeNode | None):
        if root == None:
            return

        self.dfs(root.left, root, parent)
        if grandparent != None and grandparent.val % 2 == 0:
            self.sum += root.val
        self.dfs(root.right, root, parent)
