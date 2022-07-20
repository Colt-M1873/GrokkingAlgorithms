# https://leetcode.com/problems/number-of-islands/submissions/
# 2022年07月17日 14:07:00

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def drownIsland(grid, x, y):
            grid[x][y]='0'
            directions=[[1,0],[0,1],[-1,0],[0,-1]]
            for d in directions:
                newx,newy = x+d[0],y+d[1]
                if 0<=newx<len(grid) and 0<=newy<len(grid[0]) and int(grid[newx][newy])==1:
                    drownIsland(grid,newx,newy)
            
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if int(grid[i][j])==1:
                    drownIsland(grid,i,j)
                    count+=1
        return count