# https://leetcode.cn/problems/trim-a-binary-search-tree/
# 2022年09月10日 19:21:15

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # 思路很简答， 因为是二叉搜索数，在中序遍历的时候是递增的，也即左中右递增，
        # 因此在中序遍历的时候，如果遇到小于low的节点，直接赋值成其右节点，
        # 如果遇到大于high的节点，直接赋值成其左节点

        # 没有思路的时候先默写一遍循环和递归的遍历程序， 然后可能就有思路了
        def recDFS(root):
            return recDFS(root.left)+[root.val]+recDFS(root.right) if root else []
        # print(recDFS(root))

        # v0.9 错在没有完全递归，低于或者高于的情况没有加入到递归中去
        # def recTrim(root):
        #     if not root: return root
        #     if root.val<low:
        #         return root.right
        #     elif root.val>high:
        #         return root.left
        #     else:
        #         root.left=recTrim(root.left)
        #         root.right=recTrim(root.right)
        #         return root
        #     return root

        # v1.0 递归解决，快速
        def recTrim(root):
            if not root: return root
            if root.val<low:
                return recTrim(root.right)
            elif root.val>high:
                return recTrim(root.left)
            else:
                root.left=recTrim(root.left)
                root.right=recTrim(root.right)
                return root
            return root
        ret=recTrim(root)
        return ret



        # v2 ciopeid https://leetcode.cn/problems/trim-a-binary-search-tree/solution/by-ac_oier-help/
        def iteTrim(root):
            while root and (root.val<low or root.val>high):
                if root.val<low:
                    root=root.right
                elif root.val>high:
                    root=root.left
            ret=root
            while root:
                while root.left and root.left.val<low:
                    root.left=root.left.right
                root=root.left
            root=ret
            while root:
                while root.right and root.right.val>high:
                    root.right=root.right.left
                root=root.right
            return ret
        # ret=iteTrim(root)
        # return ret

