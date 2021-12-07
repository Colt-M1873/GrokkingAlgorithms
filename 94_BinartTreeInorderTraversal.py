# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # v1 Recursive inorder traversal
        if root == None:
            return []
        ret=[root.val]
        if root.left:
            ret=self.inorderTraversal(root.left)+ret
        if root.right:
            ret=ret+self.inorderTraversal(root.right)
        return ret

        # v2 loop, non-recursive