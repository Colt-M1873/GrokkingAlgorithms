# https://leetcode.com/problems/house-robber/
# 2022年07月12日 14:19:43

class Solution:
    def rob(self, nums: List[int]) -> int:
        # v1 DP list
        dp=nums.copy() # dp recording max money till now
        if len(nums)<=2:
            return max(nums)
        dp[1]=max(dp[0],dp[1]) # ensure dp recording the max money till now
        for idx in range(2,len(dp)):
            dp[idx]=max(dp[idx]+dp[idx-2], dp[idx-1])
            # on each house, there are two choices
            # 1: rob it, that means curren money = dp[idx]+dp[idx-2]
            # 2: leave it, that means curren money = dp[idx-1]
        return dp[-1]

        # 2022年07月13日 12:05:11
        dp=nums.copy()
        if len(nums)>1:
            dp[1]=max(dp[:2])
        for i in range(2,len(nums)):
            dp[i]=max(dp[i-1],dp[i-2]+dp[i])
        return dp[-1]