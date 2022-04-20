# https://leetcode.com/problems/binary-search-tree-iterator/
# 2022年04月20日 16:10:58


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.p=TreeNode(-1)
        self.stack=[]
        self.c=root
        
        # 遇事不决先背一遍中序遍历，然后发现这道题本质就是把中序遍历拆开
        # while stack or c:
        #     while c:
        #         stack.append(c)
        #         c=c.left
        #     c=stack.pop()
        #     ret.append(c)
        #     c=c.right
        

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            while self.c:
                self.stack.append(self.c)
                self.c=self.c.left
            self.p=self.stack.pop()
            self.c=self.p
            self.c=self.c.right
        return self.p.val
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.stack or self.c:
            return True
        return False
        
# though you've solved this solution, StefanPochmann's explanation is more clear and precise 
# https://leetcode.com/problems/binary-search-tree-iterator/discuss/52647/Nice-Comparison-(and-short-Solution)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()