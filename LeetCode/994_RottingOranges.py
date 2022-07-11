# https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # # illustration
        # for item in grid:
        #     print(item)
        
        # # v1 two-pass BFS with one-pass matrix traversal, chaos, 135ms
        # # first pass:
        # # 1 find all 4-connected areas while recording all inital rotten  oranges in rot_q
        # # 2 decide if there are unrotable areas, i.e rot_q==0, if so ,return -1
        # # 3 get all inital rotten oranges in rot_q
        # # second pass:
        # # see rot_q as root of a tree, 
        # # using BFS to find all leave node (i.e fresh orages) and rot those leave node
        # # while recording the level of this tree, max level is the time cost of this area
        # def BFSqueue(grid,x,y,seen):
        #     rot_q=[]
        #     q=[(x,y)]
        #     # BFS using queue to find the whole area and record all inital rot in rot_q
        #     while q:
        #         cx,cy=q.pop(0) # currx curry
        #         if grid[cx][cy]==2:
        #             rot_q.append((cx,cy,0))
        #         for dire in [(-1,0),(0,-1),(1,0),(0,1)]:
        #             newx,newy=cx+dire[0],cy+dire[1]
        #             if (newx,newy) not in seen and 0<=newx<len(grid) and 0<=newy<len(grid[newx]) and grid[newx][newy]!=0:
        #                 seen.append((newx,newy))
        #                 q.append((newx,newy))
        #     # print('initalrot = ',len(rot_q))
        #     if not rot_q:
        #         return -1,seen
        #     else:
        #         # BFS, using tree BFS traversal with level
        #         # rot_q can be seen as root node with level of 0
        #         # total time of rot is to see max level in the rot tree of this area
        #         maxlevel=0
        #         while rot_q:
        #             cx,cy,level=rot_q.pop(0)
        #             maxlevel=max(maxlevel,level)
        #             for dire in [(-1,0),(0,-1),(1,0),(0,1)]:
        #                 newx,newy=cx+dire[0],cy+dire[1]
        #                 # find adjacent fresh oranges, i.e gridxy==1
        #                 if 0<=newx<len(grid) and 0<=newy<len(grid[newx]) and grid[newx][newy]==1:
        #                     rot_q.append((newx,newy,level+1))
        #                     grid[newx][newy]=2 # rot
        #         # print('maxlev',maxlevel)
        #         return maxlevel, seen            
        # # maincode
        # seen=[]
        # timeList=[0] # inital 0 in case of empty arg in returning max()
        # for x in range(len(grid)):
        #     for y in range(len(grid[x])):
        #         if grid[x][y]!=0 and (x,y) not in seen:
        #             seen.append((x,y))
        #             time,seen=BFSqueue(grid,x,y,seen)
        #             if time == -1:
        #                 return time
        #             else:
        #                 timeList.append(time)
        # return max(timeList)


        # v1.1 one-pass BFS with two-pass matrix traversal, 56ms, faster
        # 1) As for a 4-connected area with one original rotten orange, time of rotting within this area can be seen as the level of an quad-tree rooted at that original rotten orange
        # Similarly, multiple original rotten oreanges can be seen as roots of multiple quad-trees
        # So, first we traverse whole matrix and record all originall rotten oranges in rot_q
        # 2) The rotting process is 4-directional, i.e the quad-tree can be grown 4-directionally with adjacent fresh orages 1, and can't do anything with empty cell 0.
        # So, second we use BFS queue to grow those quad-trees according to discription above 
        # 3) after rotting process ,check if there are any fresh oranges
        # So, finally we traverse again to check remnant fresh oranges
        rot_q=[] # recording rotten orages in this queue
        maxlevel=0 # max level of all rotting trees, i.e max time
        # 1 original status: matrix traversal getting all initally rotten oranges
        for x in range(len(grid)):
            for y in range(len(grid[x])): 
                if grid[x][y]==2:
                    rot_q.append((x,y,0)) # record root node with level 0
        # 2 rotting process: BFS multi quad-tree traversal while recording maxlevel 
        while rot_q:
            cx,cy,level=rot_q.pop(0)
            maxlevel=max(maxlevel,level)
            for dire in [(-1,0),(0,-1),(1,0),(0,1)]:
                newx,newy=cx+dire[0],cy+dire[1]
                # find adjacent fresh oranges, i.e gridxy==1
                if 0<=newx<len(grid) and 0<=newy<len(grid[newx]) and grid[newx][newy]==1:
                    rot_q.append((newx,newy,level+1))
                    grid[newx][newy]=2 # rot
        # 3 end status: matrix traversal check if there are unrottable oranges
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y]==1:
                    return -1
        return maxlevel