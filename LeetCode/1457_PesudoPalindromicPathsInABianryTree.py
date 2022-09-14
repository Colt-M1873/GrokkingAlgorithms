# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
# 2022年09月14日 14:04:42

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        # find and record all possible paths, judging path in the leaf node
        
        # recursive DFS
        def recDFS(root,path):
            if not root: return 0
            path=path.copy() # note: need to get a separate copy of path in case that different recursion modifing the same dictionary
            if root.val not in path:
                path[root.val]=True
            else:
                del path[root.val]
                
            if root.left==None and root.right==None:
                if len(path) in [0,1]: 
                    return 1
                else:
                    return 0
            
            leftval=recDFS(root.left,path)
            rightval=recDFS(root.right,path)
            # print("root",root.val)
            # print("left",leftval)
            # print("right",rightval)
            # print(path)
            return leftval+rightval
        
        return recDFS(root,{})
        
        
        
    