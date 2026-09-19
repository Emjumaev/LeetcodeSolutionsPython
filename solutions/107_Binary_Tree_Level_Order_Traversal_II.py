# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
        if root == None:
            return []
        
        res = []
        queue = deque()
        queue.append(root)

        while queue:
            values = []
            for _ in range(len(queue)):
                popedElement = queue.popleft()
                if popedElement.left:
                    queue.append(popedElement.left)
                if popedElement.right:
                    queue.append(popedElement.right)

                values.append(popedElement.val)
            
            res.append(values)

        return res[::-1]
