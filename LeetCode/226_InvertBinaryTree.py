# https://leetcode.com/problems/invert-binary-tree/
# 2022年04月29日 15:07:58

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # # v1 recursion
        # if not root: return None
        # root.left, root.right = self.invertTree(root.right) ,self.invertTree(root.left)
        # return root
        
        # # v2 iterative  tobefinished
        # if not root: return None
        # queue = [root]
        # while queue:
        #     node = queue.pop(0)
        #     node.left, node.right = node.right, node.left
        #     if node.left: queue.append(node.left)
        #     if node.right: queue.append(node.right)
        # return root
        
        # v3 copied dfs using stack      
        # https://leetcode.com/problems/invert-binary-tree/discuss/62714/3-4-lines-Python  
        s=[root]
        while s:
            curr=s.pop()
            if curr:
                curr.left,curr.right=curr.right,curr.left
                s+=curr.left,curr.right
        return root
        