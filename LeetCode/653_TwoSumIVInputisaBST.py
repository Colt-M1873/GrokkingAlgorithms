# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
# 2022年06月09日 21:17:44

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # #v1  inorder traversal and hash table, 140ms
        # d={}
        # stack=[]
        # while stack or root:
        #     while root:
        #         stack.append(root)
        #         root=root.left
        #     root=stack.pop()
        #     if root.val in d:
        #         return True
        #     d[k-root.val]=True
        #     root=root.right
        # return False
        
        
        # # v2 copied, two pointer way faster 79ms
        # # https://leetcode.com/problems/two-sum-iv-input-is-a-bst/discuss/1420711/C%2B%2BJavaPython-3-solutions%3A-HashSet-Stack-Python-yield-Solutions-O(H)-space
        # def pushLeft(st, root):
        #     while root:
        #         st.append(root)
        #         root = root.left

        # def pushRight(st, root):
        #     while root:
        #         st.append(root)
        #         root = root.right

        # def nextLeft(st):
        #     node = st.pop()
        #     pushLeft(st, node.right)
        #     return node.val

        # def nextRight(st):
        #     node = st.pop()
        #     pushRight(st, node.left)
        #     return node.val

        # stLeft, stRight = [], []
        # pushLeft(stLeft, root)
        # pushRight(stRight, root)

        # left, right = nextLeft(stLeft), nextRight(stRight)
        # while left < right:
        #     if left + right == k: return True
        #     if left + right < k:
        #         left = nextLeft(stLeft)
        #     else:
        #         right = nextRight(stRight)
        # return False


        # v3 copied 70ms
        # https://leetcode.com/problems/two-sum-iv-input-is-a-bst/discuss/106067/C%2B%2BPython-Straight-Forward-Solution
        if not root: return False
        bfs, s = [root], set()
        for i in bfs:
            if k - i.val in s: return True
            s.add(i.val)
            if i.left: bfs.append(i.left)
            if i.right: bfs.append(i.right)
        return False