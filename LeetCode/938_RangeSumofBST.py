# https://leetcode.com/problems/range-sum-of-bst/
# 2021 12.14

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # # v1 recursive 260ms
        # if not root:
        #     return 0
        # if root.val>=low and root.val<=high:
        #     sum=root.val
        # else:
        #     sum=0
        # if root.left:
        #     sum+=self.rangeSumBST(root.left,low,high)
        # if root.right:
        #     sum+=self.rangeSumBST(root.right,low,high)
        # return sum

        # v1.1 clear recursive, 192ms, also using inorfer ascending order
        if not root: return 0
        if root.val > high: return self.rangeSumBST(root.left,low,high)
        if root.val < low: return self.rangeSumBST(root.right,low,high)
        return root.val + self.rangeSumBST(root.left,low,high) + self.rangeSumBST(root.right,low,high)      

        # # v2 iterative using stack 256ms
        # sum=0
        # stack=[]
        # while stack or root:
        #     while root:
        #         stack.append(root)
        #         root=root.left
        #     root=stack.pop()
        #     if root.val<=high and root.val >= low:
        #         sum+=root.val
        #     root=root.right
        # return sum

        # # v2.1 iterative using stack 184ms, 
        # # improved speed by knowing that input tree is ascending when doing inorder traversal
        # sum=0
        # stack=[]
        # while stack or root:
        #     while root:
        #         stack.append(root)
        #         if root.val<low:
        #             break
        #         root=root.left
        #     root=stack.pop()
        #     if root.val<=high and root.val >= low:
        #         sum+=root.val
        #     if root.val>high:
        #         break
        #     root=root.right
        # return sum

        # # v2.2 clean iterative 208ms
        # stack = [root]
        # ans = 0
        # while(stack):
        #     node = stack.pop()
        #     if node:
        #         if low <= node.val <= high: ans += node.val
        #         if low < node.val: stack.append(node.left)
        #         if high > node.val: stack.append(node.right)
        # return ans