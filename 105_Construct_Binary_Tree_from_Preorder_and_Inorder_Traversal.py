# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None

        rootNode = TreeNode(preorder[0])

        index = inorder.index(preorder[0])

        inorderLeft = inorder[0:index]
        inorderRight = inorder[(index + 1):]

        preorderLeft = preorder[1:(index + 1)]
        preorderRight = preorder[(index + 1):]

        rootNode.left = self.buildTree(preorderLeft, inorderLeft)
        rootNode.right = self.buildTree(preorderRight, inorderRight)

        return rootNode
