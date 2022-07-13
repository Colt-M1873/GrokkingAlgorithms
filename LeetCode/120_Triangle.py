# https://leetcode.com/problems/triangle/
# 2022年07月12日 14:42:45

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # v1 DP
        # dp list recording the minimum of each path till last row
        dp=triangle[0].copy()
        for row in triangle[1:]: # do not include the first line cause it's the inital DP condition
            for idx in range(len(row)):
                if idx==0: # in the beginning of each row
                    row[idx] += dp[idx] # only upper right val can be selected
                elif idx==len(row)-1: # in the end of each row
                    row[idx] += dp[idx-1] # only upper left val can be selected
                else: # in the middle
                    row[idx] += min(dp[idx],dp[idx-1]) 
                    # choose the min between upper left and upper right val in dp list of last row
            dp=row.copy() # update dp
        return min(dp)