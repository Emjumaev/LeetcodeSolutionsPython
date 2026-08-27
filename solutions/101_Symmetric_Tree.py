# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        queue = []
        queue.append(root)

        while(queue):
            for i in range(len(queue)):
                popedItem = queue.pop(0) # Dequeue
                if popedItem == None:
                    continue
                queue.append(popedItem.left)
                queue.append(popedItem.right)

            # check for symmetry
            left = 0
            right = len(queue) - 1
            while(left < right):
                leftVal = -101
                if queue[left] != None:
                    leftVal = queue[left].val

                rightVal = -101
                if queue[right] != None:
                    rightVal = queue[right].val

                if leftVal != rightVal:
                    return False

                left += 1
                right -= 1

        return True
