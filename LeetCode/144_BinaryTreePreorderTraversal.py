# https://leetcode.com/problems/binary-tree-preorder-traversal/
#  2022年04月14日 17:37:19


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # # v1 recursive
        # if not root : return []
        # ret=[root.val]
        # if root.left:
        #     ret=ret+self.preorderTraversal(root.left)
        # if root.right:
        #     ret=ret+self.preorderTraversal(root.right)
        # return ret
    
        # v2 recursive oneliner
        return [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right) if root else []

        # 调整进出栈或者队列的顺序
        # v2 copied, iterative using stack, superfast
        stack=[root]
        ret=[]
        while stack :
            curr=stack.pop()
            if curr:
                ret.append(curr.val)
                stack.append(curr.right)
                stack.append(curr.left)
        return ret

