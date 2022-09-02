# https://leetcode.cn/problems/longest-univalue-path/
# 2022年09月02日 07:46:02

# v1 recursive DFS
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        currMax=0
        def recursiveDFS(root):
            if not root : return 0
            leftMax=recursiveDFS(root.left)
            righMax=recursiveDFS(root.right)
            if root.left and root.val==root.left.val:
                leftMax+=1
            else:
                leftMax=0
            if root.right and root.val==root.right.val:
                righMax+=1
            else:
                righMax=0
            nonlocal currMax
            currMax=max(currMax,leftMax+righMax)
            return max(leftMax,righMax)
        recursiveDFS(root)
        return currMax

# v1.1 recursive without local variable
    def longestUnivaluePath(self, root):
        def recDFS2(root):
            if not root: return 0, 0
            maxL, pathL  = recDFS2(root.left)
            maxR, pathR = recDFS2(root.right)        
            pathL = pathL + 1 if root.left and root.left.val == root.val else 0
            pathR = pathR+ 1 if root.right and root.right.val == root.val else 0
            return max(maxL, maxR, pathL + pathR), max(pathL, pathR)
        return recDFS2(root)[0]



# v2 iterative post-order DFS
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        currMax = 0
        postorder = [(0, root, None)]
        d = {None: 0}
        while postorder:
            seen, node, parent = postorder.pop()
            if not node: continue
            if not seen:
                postorder.append((1, node, parent))
                postorder.append((0, node.right, node.val))
                postorder.append((0, node.left, node.val))
            else:
                if node.val == parent:
                    d[node] = max(d[node.left], d[node.right]) + 1
                else:
                    d[node] = 0
                currMax = max(currMax, d[node.left] + d[node.right])
        return currMax
     