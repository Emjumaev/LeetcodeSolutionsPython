# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.hashMap = {}
        res = []

        self.dfs(root)

        maxFreq = max(self.hashMap.values())
        for i, v in self.hashMap.items():
            if v == maxFreq:
                res.append(i)

        return res

    def dfs(self, root: Optional[TreeNode]):
        if root == None:
            return

        if root.val in self.hashMap:
            self.hashMap[root.val] += 1
        else:
            self.hashMap[root.val] = 0

        self.dfs(root.left)
        self.dfs(root.right)
