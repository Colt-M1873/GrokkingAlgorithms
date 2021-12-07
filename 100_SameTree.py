# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # # v1 copied recursion
        # if p==None and q==None:
        #     return True
        # if p and q:
        #     if p.val==q.val:
        #         return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        #     else:
        #         return False
        # else :
        #     return False

        # v1.1 copied recursion  more clear
        if not p and not q: # p and q are both None
            return True
        if not p or not q: # one of p and q is None
            return False
        if p.val!=q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right , q.right)

        # v2 iteretive  non-recursive





        # # v3 Stefan Pochmann 
        # if p and q:
        #     return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # return p is q

        # # v3.1 Stefan Pochmann 
        # def t(n):
        #     return n and (n.val, t(n.left), t(n.right))
        # return t(p) == t(q)

        # # v3.2 sick oneliner by Stefan Pochmann
        # return p and q and p.val == q.val and all(map(self.isSameTree, (p.left, p.right), (q.left, q.right))) or p is q