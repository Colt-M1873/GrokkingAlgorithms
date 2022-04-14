# https://leetcode.com/problems/binary-tree-inorder-traversal/
# 2021 12.07

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # # v1 Recursive inorder traversal
        # if root == None:
        #     return []
        # ret=[root.val]
        # if root.left:
        #     ret=self.inorderTraversal(root.left)+ret
        # if root.right:
        #     ret=ret+self.inorderTraversal(root.right)
        # return ret

        # # v1.1 recursive oneliner
        # return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right) if root else []

        # v2 copied iterative, non-recursive using stack
        ret =[]
        stack=[]
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root=stack.pop()
            ret.append(root.val)
            root=root.right
        return ret