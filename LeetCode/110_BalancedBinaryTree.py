# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # v1 recursive using Q104 and check if each node is balanced 
        if not root:
            return True
        def maxDepth(root):
            return 1+max(maxDepth(root.left),maxDepth(root.right)) if root else 0
        if abs(maxDepth(root.left)-maxDepth(root.right))<=1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False
