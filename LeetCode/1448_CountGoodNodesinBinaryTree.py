# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# 2022年09月01日 18:02:10

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # dfs recursive
        def recursion(root, currMax):
            if not root: return 0
            good=0
            if root.val>=currMax:
                currMax=root.val
                good=1
            good+=(recursion(root.left,currMax)+recursion(root.right,currMax))
            return good
        return recursion(root,root.val)