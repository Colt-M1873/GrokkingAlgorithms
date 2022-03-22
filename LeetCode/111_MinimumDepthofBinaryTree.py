# https://leetcode.com/problems/minimum-depth-of-binary-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # # v1 slow recursive using method in Q104 maxDepth and modified , 600ms
        # if not root:
        #     return 0
        # while root.left and not root.right:
        #     return 1+self.minDepth(root.left) 
        # while root.right and not root.left:
        #     return 1+self.minDepth(root.right) 
        # return 1+min(self.minDepth(root.left),self.minDepth(root.right))

        # # v1.1 copied recursive Stefan Pochmann super short but need to first understand v1
        # # when root has both left and right, d=(1,1), so (min(d) or max(d))==1
        # # when root only has left or right, d=(0,1) or d=(1,0), so (min(d) or max(d))==1
        # # when root left and right are both none, (min(d) or max(d))==0
        # if not root: return 0
        # d = list(map(self.minDepth, (root.left, root.right)))
        # return 1 + (min(d) or max(d))

        # v2 copied BFS, fast  450ms 
        if not root:
            return 0
        queue=[(root,1)]
        while queue:
            node,level=queue.pop(0)
            if node:
                if not node.left and not node.right:
                    return level
                else:
                    queue.append((node.left,level+1))
                    queue.append((node.right,level+1))
