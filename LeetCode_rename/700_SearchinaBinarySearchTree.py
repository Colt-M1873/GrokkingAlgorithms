# https://leetcode.com/problems/search-in-a-binary-search-tree/
# 2022年04月14日 15:40:04

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        # v1 iterative use queue to do BFS
        q=[root]
        curr=root
        while q:
            curr=q.pop(0)
            if curr.val==val: return curr
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return None 

        # v2 recursive
        if not root: return None
        if root.val==val: return root
        return self.searchBST(root.left,val) or self.searchBST(root.right,val)

        # v2.1 recursive oneliner        
        return root if (not root or root.val==val) else (self.searchBST(root.left,val) or self.searchBST(root.right,val))
    


        # v3 copied, use the feature of BST
        # binary search tree is different from binary tree
        # BST is a binary tree where each node has a value greater than or equal to its left child and less than or equal to its right child
        # use this feature of BST
        # compare the value of curr node and target value
        # theoretically faster than previous methods
        curr=root
        while curr:
            if curr.val==val: return curr
            elif curr.val>val:
                curr=curr.left
            else:
                curr=curr.right
        return curr