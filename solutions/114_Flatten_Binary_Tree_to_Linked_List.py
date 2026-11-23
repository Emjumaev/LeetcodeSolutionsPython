# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.preorder = []
        self.preorderDFS(root)

        for i in range(len(self.preorder) - 1):
            node = self.preorder[i]
            node.right = self.preorder[i + 1]
            node.left = None

    def preorderDFS(self, root: Optional[TreeNode]):
        if root == None:
            return

        self.preorder.append(root)
        self.preorderDFS(root.left)
        self.preorderDFS(root.right)
