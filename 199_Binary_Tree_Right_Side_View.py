# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []

        res = []
        queue = []

        queue.append(root)

        while(len(queue) != 0):
            level = []

            for i in range(0, len(queue)):
                popedNode = queue.pop(0)

                level.append(popedNode.val)

                if popedNode.left != None:
                    queue.append(popedNode.left)
                if popedNode.right != None:
                    queue.append(popedNode.right)

            res.append(level[-1])

        return res
