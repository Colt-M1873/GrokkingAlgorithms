# https://leetcode.com/problems/longest-increasing-subsequence
# 2022 2.22

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # v1, copied dp, slow, 5600ms
        dp=[1]*len(nums)
        for i in range(0,len(nums)):
            for j in range(0,i-1):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
            # print(dp)
        return max(dp)
