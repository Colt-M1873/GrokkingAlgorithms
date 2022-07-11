# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
# 2022年07月09日 13:58:49


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        #v1  BFS using queue, recording the level of each node
        if not root: return None
        level=0
        q=[(root,level)]
        # ret=[(root.val,level)]
        while q:                
            curr,lev = q.pop(0)
            # ret.append((curr.val,lev))
            if not q or lev!=q[0][1]:
                curr.next=None
            else:
                curr.next=q[0][0]
            lev+=1
            if curr.left:
                q.append((curr.left,lev))
            if curr.right:
                q.append((curr.right,lev))
        # print(ret)
        return root


        # # v2 copied StefanPochmann
        # # https://leetcode.com/problems/populating-next-right-pointers-in-each-node/discuss/37484/7-lines-iterative-real-O(1)-space
        # ret=root
        # while root and root.left:
        #     nextNode = root.left
        #     while root:
        #         root.left.next = root.right
        #         root.right.next = root.next and root.next.left
        #         root = root.next
        #     root = nextNode
        # return ret


        # v2 DFS
        # https://leetcode.com/problems/populating-next-right-pointers-in-each-node/discuss/37715/Python-solutions-(Recursively-BFS%2Bqueue-DFS%2Bstack)