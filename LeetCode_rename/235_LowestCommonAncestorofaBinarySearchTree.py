# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree
# 2022年05月19日 19:06:41

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # recite in-order dfs
        # 思考如何记录path
        # https://blog.csdn.net/abcdef314159/article/details/109191658
        # 你想通过在dfs中记录当前path的方法来做，但未成功，待完善
        # ret=[]
        # curr=root
        # stack=[]
        # currpath=[]
        # while stack or curr:
        #     while curr:
        #         currpath.append(curr.val)
        #         stack.append(curr)
        #         curr=curr.left
        #     curr=stack.pop()
        #     currpath.pop()
        #     if curr==p:
        #         print(p.val,"currpath ",currpath)
        #     if curr==q:
        #         print(q.val,"currpath ",currpath)
        #     ret.append(curr.val)
        #     currpath.append(curr.val)
        #     curr=curr.right
        # print(ret)
        # return 0
        
        # v2 copied iterative
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root
            
        # # v2.1 copied recursive
        # if root.val > p.val and root.val > q.val:
        #     return self.lowestCommonAncestor(root.left,p,q)
        # if root.val < p.val and root.val < q.val:
        #     return self.lowestCommonAncestor(root.right,p,q)
        # return root
        