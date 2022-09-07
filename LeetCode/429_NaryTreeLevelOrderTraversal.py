# https://leetcode.com/problems/n-ary-tree-level-order-traversal/
# 2022年09月05日 15:04:19
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # v1 BFS using queue
        if not root: return []
        q=[(root,0)]
        ret=[]
        while q:
            node,layer=q.pop(0)
            if node:
                for c in node.children:
                    q.append((c,layer+1))
            if not ret or len(ret)<layer+1:
                ret.append([node.val])
            else:
                ret[layer].append(node.val)
        return ret
                