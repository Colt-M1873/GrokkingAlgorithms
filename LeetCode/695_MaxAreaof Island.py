# https://leetcode.com/problems/max-area-of-island/\
# 2022年07月07日 19:49:14

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # 4 connected area, can be seen as quad-tree
        # v1 DFS with recursion
        def countAreaDFSrecursion(grid,x,y):
            area=1
            if grid[x][y]==1:
                grid[x][y]=2
                if x-1>=0:
                    area+=countAreaDFSrecursion(grid,x-1,y)
                if y-1>=0:
                    area+=countAreaDFSrecursion(grid,x,y-1)
                if x+1<len(grid):
                    area+=countAreaDFSrecursion(grid,x+1,y)
                if y+1<len(grid[x]):
                    area+=countAreaDFSrecursion(grid,x,y+1)
                return area
            else:
                return 0
        
        # v2 BFS using queue
        def countAreaBFSqueue(grid,a,b):
            q=[(a,b)]
            area=0
            while q:
                curr_x=q[0][0]
                curr_y=q[0][1]
                grid[curr_x][curr_y]=2
                if curr_x-1>=0 and grid[curr_x-1][curr_y]==1:
                    q.append((curr_x-1,curr_y))
                    grid[curr_x-1][curr_y]=2
                if curr_y-1>=0 and grid[curr_x][curr_y-1]==1:
                    q.append((curr_x,curr_y-1))
                    grid[curr_x][curr_y-1]=2
                if curr_x+1<len(grid) and grid[curr_x+1][curr_y]==1:
                    q.append((curr_x+1,curr_y))
                    grid[curr_x+1][curr_y]=2
                if curr_y+1<len(grid[curr_x]) and grid[curr_x][curr_y+1]==1:
                    q.append((curr_x,curr_y+1))
                    grid[curr_x][curr_y+1]=2
                q.pop(0)
                area+=1
            return area
        
        # v3 DFS with stack
        def countAreaDFSstack(grid,a,b):
            s=[(a,b)]
            area=0
            while s:
                (curr_x,curr_y)=s.pop()
                grid[curr_x][curr_y]=2
                if curr_x-1>=0 and grid[curr_x-1][curr_y]==1:
                    s.append((curr_x-1,curr_y))
                    grid[curr_x-1][curr_y]=2
                if curr_y-1>=0 and grid[curr_x][curr_y-1]==1:
                    s.append((curr_x,curr_y-1))
                    grid[curr_x][curr_y-1]=2
                if curr_x+1<len(grid) and grid[curr_x+1][curr_y]==1:
                    s.append((curr_x+1,curr_y))
                    grid[curr_x+1][curr_y]=2
                if curr_y+1<len(grid[curr_x]) and grid[curr_x][curr_y+1]==1:
                    s.append((curr_x,curr_y+1))
                    grid[curr_x][curr_y+1]=2
                area+=1
            return area
        
        
        # main code 2-D array traversal
        areaList=[0] # set a default 0 to avoid empty list in the returning max()
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y]==1:
                    # areaList.append(countAreaDFSrecursion(grid,x,y)) # v1 DFS recursion          
                    areaList.append(countAreaBFSqueue(grid,x,y)) # v2 BFS queue
                    # areaList.append(countAreaDFSstack(grid,x,y)) # v3 DFS stack
        # # Demonstrate
        # for item in grid:
        #     print(item)
        return max(areaList)
    
    
        
        
      