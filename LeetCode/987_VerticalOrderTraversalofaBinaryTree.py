# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
# 2022年09月04日 18:34:14


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # recite inorder dfs
        ret=[]
        stack=[]
        root.val=[root.val, 0, 0]# originalval, row, col
        while stack or root:
            while root:
                stack.append(root)                
                lastRow=root.val[1]
                lastCol=root.val[2]
                root=root.left
                if root:
                    root.val=[root.val,lastRow+1,lastCol-1]
            root=stack.pop()
            ret.append(root.val)
            lastRow=root.val[1]
            lastCol=root.val[2]
            root=root.right
            if root:
                root.val=[root.val, lastRow+1, lastCol+1]
        ret.sort(key=lambda x:(x[2],x[1],x[0])) # multiple key, first sory by col, then by row, then by value 用其他语言实现多Key排序？？
        # print(ret)
        ans=[]
        currCol=None
        for item in ret:
            if item[2]!=currCol:
                ans.append([item[0]])
                currCol=item[2]
            else:
                ans[-1].append(item[0])
        # print(ans)
        return ans
                
            
            