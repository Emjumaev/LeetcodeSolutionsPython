# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.inorder = []
        self.inorderDFS(root)

        res = float('inf')

        for i in range(1, len(self.inorder)):
            diff = abs(self.inorder[i] - self.inorder[i - 1])
            res = min(res, diff)

        return res

    def inorderDFS(self, root: TreeNode | None):
        if root == None:
            return

        self.inorderDFS(root.left)
        self.inorder.append(root.val)
        self.inorderDFS(root.right)
