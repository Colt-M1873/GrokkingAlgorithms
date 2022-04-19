# https://leetcode.com/problems/recover-binary-search-tree/
# 2022年04月19日 12:50:57


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # # recite inorder traversal
        # s=[]
        # c=root
        # ret=[]
        # while s or c:
        #     while c:
        #         s.append(c)
        #         c=c.left
        #     c=s.pop()
        #     ret.append(c.val)
        #     c=c.right
        # print(ret)
        # return ret
    
    
        # v1 inorder traversal extend
        # 如果BST出错，并且如题中所说有两个互换出错，那用比大小来查错只有一种情况
        # 因为BST是递增的，所以只需要排查后比前小（decrease）的情况，而decrease可能出现一次或者两次
        # 如果decrease出现两次的话，第一次出现后比前小，则出错在前，第二次出现后比前小，出错在后，将一次的前和二次的后对换即可
        # 如果decrease只出现一次的话，表明相邻元素前后互换即可获得结果
        wrongnode=[]
        decreasecount=0
        last=None
        stack=[]
        curr=root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr=curr.left
            curr=stack.pop()
            # 初始last不能等于root，因为第一个curr是出现在最左端的，如果last=root的话在正确的BST里curr也是小于last的
            # 所以初始last=None，并且让last等于第一个curr
            if not last:
                last=curr
            ##在中序遍历的基础上检测后一个比前一个小decrease的情况##
            if curr.val<last.val:
                decreasecount+=1
                if not wrongnode:
                    wrongnode.append(last) # 解决那种decrease只出现一次，相邻元素互换的情况
                    wrongnode.append(curr) #
                else:
                    wrongnode[1]=curr
            if decreasecount==2: # 如果查找到两侧decrease，则已找全，可立即退出
                break
            last=curr
            ###########################################
            curr=curr.right
        wrongnode[0].val, wrongnode[1].val =wrongnode[1].val, wrongnode[0].val
        
        
        # v2 recursive 
        # https://leetcode.com/problems/recover-binary-search-tree/discuss/32562/Share-my-solutions-and-detailed-explanation-with-recursiveiterative-in-order-traversal-and-Morris-traversal
        


        
        # v3  Morris traversal 
        # https://leetcode.com/problems/recover-binary-search-tree/discuss/32559/Detail-Explain-about-How-Morris-Traversal-Finds-two-Incorrect-Pointer