# https://leetcode.com/problems/increasing-order-search-tree/
# 2022年04月17日 21:29:37


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # # v1 iterative
        # ret=[]
        # stack=[]
        # while stack or root:
        #     while root:
        #         stack.append(root)
        #         root=root.left
        #     root=stack.pop()
        #     ret.append(root)
        #     root=root.right
        # ret.append(None)
        # for i in range(len(ret)-1):
        #     ret[i].left=None
        #     ret[i].right=ret[i+1]
        # return ret[0]        
        
        # v2 recursive
        def rec(root):
            if not root: return []
            return rec(root.left)+[root]+rec(root.right)
        ret=rec(root)
        ret.append(None)
        for i in range(len(ret)-1):
            ret[i].left=None
            ret[i].right=ret[i+1]
        return ret[0]    
        