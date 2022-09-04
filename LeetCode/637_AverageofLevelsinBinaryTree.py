# https://leetcode.com/problems/average-of-levels-in-binary-tree/
# 2022年09月02日 11:51:36

# v1 bfs using queue
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # bfs using queue
        q=[(root,0)]
        lastlev=0
        levlen=1
        levsum=root.val
        ret=[]
        while q:
            curr,lev=q.pop(0)
            if lev==lastlev:
                levlen+=1
                levsum+=curr.val
            else:
                ret.append(levsum/levlen)
                levlen=1
                levsum=curr.val
                lastlev=lev
            if curr.left:
                q.append((curr.left,lev+1))
            if curr.right:
                q.append((curr.right,lev+1))
        ret.append(levsum/levlen)
        return ret