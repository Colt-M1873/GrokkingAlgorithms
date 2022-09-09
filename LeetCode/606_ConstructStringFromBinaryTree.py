# https://leetcode.com/problems/construct-string-from-binary-tree/submissions/
# 2022年09月07日 18:59:33

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def recDFS(root):
            if not root: return ''
            ret=str(root.val)
            if root.left or root.right:
                ret+="("+recDFS(root.left)+")"
            if root.right:
                ret+="("+recDFS(root.right)+")"
            return ret
        
        def iteDFS(root):
            stack=[]
            
        
        return (recDFS(root))