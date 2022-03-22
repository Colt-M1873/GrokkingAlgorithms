# https://leetcode.com/problems/maximum-subarray/
# 2021 11.29 2022 3.06 3.09
# Totally no fucking idea


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:  
        # # v1 copied
        # cur_max=glob_max=nums[0]
        # for i in range(1,len(nums)):
        #     cur_max=max(cur_max+nums[i],nums[i])
        #     glob_max=max(cur_max,glob_max)
        # return glob_max
        
        # v2 copied  DP
        dp=[0]*len(nums)
        for i in range(len(nums)):
            dp[i]=max(dp[i-1]+nums[i],nums[i])
        return max(dp)