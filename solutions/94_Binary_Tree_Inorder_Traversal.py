# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.inorderTraverse(root)
        return self.res

    def inorderTraverse(self, root: Optional[TreeNode]):
        if root == None:
            return

        self.inorderTraverse(root.left)
        self.res.append(root.val)
        self.inorderTraverse(root.right)
