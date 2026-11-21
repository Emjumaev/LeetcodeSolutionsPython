# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode | None) -> TreeNode | None:
        self.inorder = []
        self.inorderTraverse(root)

        postfixSum = []
        cur = 0
        for num in self.inorder[::-1]:
            cur += num
            postfixSum.append(cur)
        
        self.hash_map = {}
        for key, val in zip(self.inorder, postfixSum[::-1]):
            self.hash_map[key] = val

        self.updateTree(root)

        return root
        
    def inorderTraverse(self, root: TreeNode | None):
        if root == None:
            return
        
        self.inorderTraverse(root.left)
        self.inorder.append(root.val)
        self.inorderTraverse(root.right)

    def updateTree(self, root: TreeNode | None):
        if root == None:
            return
        
        self.updateTree(root.left)
        root.val = self.hash_map[root.val]
        self.updateTree(root.right)
