# https://leetcode.com/problems/merge-two-binary-trees/
# 2022年07月09日 13:57:31

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # # v1 DFS recursive
        # if not root1 and not root2: return None
        # if root1 and root2:
        #     root1.val+=root2.val
        #     if root1.left or root2.left:
        #         root1.left=self.mergeTrees(root1.left,root2.left)
        #     if root1.right or root2.right:
        #         root1.right=self.mergeTrees(root1.right,root2.right)
        # if not root1 and root2:
        #     root1=root2
        # return root1
    
        # # v1.1 copied, more concise
        # if root1 and root2:
        #     root = TreeNode(root1.val + root2.val)
        #     root.left = self.mergeTrees(root1.left, root2.left)
        #     root.right = self.mergeTrees(root1.right, root2.right)
        #     return root
        # else:
        #     return root1 or root2

        # v1.2 copied and improved with less space consumption
        if root1 and root2:
            root1.val += root2.val
            root1.left = self.mergeTrees(root1.left, root2.left)
            root1.right = self.mergeTrees(root1.right, root2.right)
            return root1
        else:
            return root1 or root2
        
        # # v1.3 copied , 3-liner recursive
        # # https://leetcode.com/problems/merge-two-binary-trees/discuss/2077828/Python3%3A-BFS.-Create-new-tree
        # if not root1: return root2
        # if not root2: return root1
        # return TreeNode(root1.val + root2.val, self.mergeTrees(root1.left, root2.left), self.mergeTrees(root1.right, root2.right))


        # v2 DFS using stack

        # v3 BFS using queue