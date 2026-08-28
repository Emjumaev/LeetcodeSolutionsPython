# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.formBST(nums)

    def formBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None

        root = TreeNode(nums[len(nums) // 2])

        root.left = self.formBST(nums[:len(nums) // 2])
        root.right = self.formBST(nums[(len(nums) // 2 + 1):])

        return root
