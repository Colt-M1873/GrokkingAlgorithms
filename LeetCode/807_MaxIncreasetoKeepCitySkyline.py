# https://leetcode.com/problems/max-increase-to-keep-city-skyline/submissions/
# 2021 12.13

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        # # v1 dumb 72ms too much useless steps
        # SouthView=list(map(max,zip(*grid)))
        # WesthView=list(map(max,grid))
        # print(SouthView)
        # print(WesthView)
        # NScapacity=[]
        # l=len(grid)
        # for i in range(l):
        #     NScapacity.append(SouthView.copy())
        # sum=0
        # for i in range(l):
        #     for j in range(l):
        #         if NScapacity[i][j]>WesthView[i]:
        #             NScapacity[i][j]=WesthView[i]
        #         sum+=NScapacity[i][j]-grid[i][j]
        # print(NScapacity)
        # return sum

        # # v2 slow 840ms, using zip in the loop slowed down the whole code
        # l=len(grid)
        # sum=0
        # for i in range(l):
        #     for j in range(l):
        #         maxheight=min(max(grid[i]),max(list(zip(*grid))[j]))
        #         if grid[i][j]<maxheight:
        #             sum+=maxheight-grid[i][j]
        # return sum

        # v2.1 faster, 68ms, just zip once 
        l=len(grid)
        sum=0
        SouthView=list(map(max,zip(*grid)))
        WesthView=list(map(max,grid))
        for i in range(l):
            for j in range(l):
                maxheight=min(SouthView[j],WesthView[i])
                if grid[i][j]<maxheight:
                    sum+=maxheight-grid[i][j]
        return sum

