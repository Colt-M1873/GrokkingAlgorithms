# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def PathSum(root,retarr,endcount):
            if not root.left and not root.right:
                print('firstendnode')
                endcount+=1
                if endcount==1:
                    retarr[0]+=root.val
                else:
                    retarr.append(root.val)
                return root,retarr,endcount
            if root.left:
                _,retarr,endcount=PathSum(root.left,retarr,endcount)
                retarr[endcount]+=root.val
            if root.right:
                _,retarr,endcount=PathSum(root.left,retarr,endcount)
                retarr[endcount]+=root.val
        sumarr=PathSum(root,[0],0)
        print(sumarr)