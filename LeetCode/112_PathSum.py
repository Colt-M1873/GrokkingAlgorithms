# https://leetcode.com/problems/path-sum/
# 2021 12.12


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # # v1 copied Iterative using stack
        # if not root:
        #     return False
        # stack=[(root,root.val)]
        # while stack:
        #     curr,val=stack.pop()
        #     if not curr.left and not curr.right and val==targetSum:
        #         return True
        #     if curr.left:
        #         stack.append((curr.left,val+curr.left.val))
        #     if curr.right:
        #         stack.append((curr.right,val+curr.right.val))
        # return False

        # v2 copied Recursive, neat and birlliant
        if not root:
            return False
        if not root.left and not root.right and root.val==targetSum:
            return True
        targetSum-=root.val
        return self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right,targetSum)