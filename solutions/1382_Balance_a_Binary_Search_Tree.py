# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode | None) -> TreeNode | None:
        self.inorderArr = []
        self.inorder(root)

        return self.constructBST(self.inorderArr)

    def constructBST(self, arr: list[int]) -> TreeNode | None:
        if len(arr) == 0:
            return None

        if len(arr) == 1:
            return TreeNode(arr[0])

        mid = (len(arr) - 1) // 2
        root = TreeNode(arr[mid])

        root.left = self.constructBST(arr[:mid])
        root.right = self.constructBST(arr[(mid + 1):])

        return root

    def inorder(self, root: TreeNode | None):
        if root == None:
            return

        self.inorder(root.left)
        self.inorderArr.append(root.val)
        self.inorder(root.right)
