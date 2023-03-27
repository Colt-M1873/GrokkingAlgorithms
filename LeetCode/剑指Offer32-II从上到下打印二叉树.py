# https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/description/?envType=study-plan&id=lcof&plan=lcof&plan_progress=flnj2s3
# 2023年03月25日 17:07:31

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        Layer=[root]
        nextLayer=[]
        ret=[]
        while Layer or nextLayer:
            layerRet=[]
            while Layer:
                curr=Layer.pop(0)
                layerRet.append(curr.val)
                if curr.left: nextLayer.append(curr.left)
                if curr.right: nextLayer.append(curr.right)
            ret.append(layerRet)
            Layer=nextLayer
            nextLayer=[]
        return ret
            
