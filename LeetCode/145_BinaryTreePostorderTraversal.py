# https://leetcode.com/problems/binary-tree-postorder-traversal/
# 2022年04月14日 17:47:23

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # # v1 recursive
        # if not root: return []
        # ret=[root.val]
        # ret=self.postorderTraversal(root.left)+self.postorderTraversal(root.right)+ret
        # return ret
        
        # # v1.1 recursive oneliner
        # return self.postorderTraversal(root.left)+self.postorderTraversal(root.right)+[root.val] if root else []
        
        
        # v2 iterative
        # 你的思路暂时是先做出一个前序遍历并且左右互换的结果出来，然后倒序输出，这样效率不太高，搜索是否有效率更高的方案
        stack=[root]
        ret=[]
        while stack:
            curr=stack.pop()
            if curr:
                ret.append(curr.val)
                stack.append(curr.left)
                stack.append(curr.right)
        return ret[::-1]
            
            