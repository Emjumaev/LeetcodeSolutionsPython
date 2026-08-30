# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.ans = []
        self.dfs(root, str(root.val))

        return self.ans

    def dfs(self, root: Optional[TreeNode], path: str):
        if root.left == None and root.right == None:
            self.ans.append(path)
            return

        if root.left != None:
            self.dfs(root.left, path + "->" + str(root.left.val))

        if root.right != None:
            self.dfs(root.right, path + "->" + str(root.right.val))
