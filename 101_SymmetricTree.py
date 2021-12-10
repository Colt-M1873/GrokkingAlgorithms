# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    # # v1 recursive like Q100 SameTree just change same to mirror
    #     return self.mirrorTree(root.left,root.right)
    
    # def mirrorTree(self,p,q):
    #     if not p and not q:
    #         return True
    #     if p and q:
    #         if p.val== q.val:
    #             return self.mirrorTree(p.left,q.right) and self.mirrorTree(p.right,q.left)
    #         else:
    #             return False
    #     else:
    #         return False

        # v2 iterative like Q100 SameTree
        stack=[(root.left,root.right)]
        while stack:
            x,y=stack.pop()
            if not x and not y:
                continue
            if not (x and y):
                return False
            if x and y:
                if x.val==y.val:
                    stack.append((x.left,y.right))
                    stack.append((x.right,y.left))
        return True