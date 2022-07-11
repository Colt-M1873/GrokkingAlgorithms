# https://leetcode.com/problems/01-matrix/
# 2022年07月10日 11:19:44


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # v1 copied, BFS using queue 
        # https://leetcode.com/problems/01-matrix/discuss/363902/BFS-python-explained-and-commneted-(two-approaches)
        q=[]
        # visited=[] # TLE
        visited=set() # search in set is faster than search in list
        # visited={} # search in dict is almost the same speed as search in set
        for x in range(len(mat)):
            for y in range(len(mat[x])):
                if mat[x][y]==0:
                    # visited.append((x,y)) # TLE
                    visited.add((x,y)) # set
                    # visited[(x,y)]=None # dict
                    q.append((x,y))
        while q:
            x,y=q.pop(0)
            for dire in [(1,0),(-1,0),(0,1),(0,-1)]:
                newx=x+dire[0]
                newy=y+dire[1]
                if (newx,newy) not in visited and newx>=0 and newy>=0 and newx<len(mat) and newy<len(mat[newx]):
                    mat[newx][newy]=mat[x][y]+1
                    # visited.append((newx,newy)) # TLE
                    visited.add((newx,newy)) # set
                    # visited[(newx,newy)]=None # dict
                    q.append((newx,newy))
                    
        return mat