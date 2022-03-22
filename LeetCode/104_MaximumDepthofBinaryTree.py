# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # # v1 tree BFS using queue, and count layer by calculationg nodes in each layer
        # if not root:
        #     return 0
        # queue=[root]
        # depth=1
        # thislayernode=1
        # while queue:
        #     current=queue.pop(0)
        #     thislayernode-=1
        #     # print(current.val)
        #     if current.left:
        #         queue.append(current.left)
        #     if current.right:
        #         queue.append(current.right)
        #     if  thislayernode==0:
        #         thislayernode=len(queue)
        #         print('this layer has {} node'.format(thislayernode))
        #         if thislayernode !=0:
        #             depth+=1
        #             print('this is the {} layer'.format(depth))
        # return depth
            
        # v2 copied Stefan Pochmann oneliner recursive
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0