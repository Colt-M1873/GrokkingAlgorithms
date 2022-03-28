# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/submissions/
# 2021 12.11

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Failed to use iterative method
        # v1 copied recursive, clear and brilliant
        if not nums:
            return None
        middle=len(nums)//2
        root=TreeNode(nums[middle])
        root.left=self.sortedArrayToBST(nums[:middle])
        root.right=self.sortedArrayToBST(nums[middle+1:])
        return root