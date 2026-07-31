# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = []
        queue.append(root)

        while(len(queue) != 0):
            pop = queue.pop(0)

            if pop == None:
                while(len(queue) != 0):
                    if queue.pop(0) != None:
                        return False
            else:
                queue.append(pop.left)
                queue.append(pop.right)

        return True

"""
Space: O(n)
Time: O(n)
"""
