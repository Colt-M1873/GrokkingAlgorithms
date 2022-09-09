# https://leetcode.cn/problems/longest-continuous-increasing-subsequence/
# 2022年09月08日 14:33:27

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        dp=[1]*len(nums)
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                dp[i]=dp[i-1]+1
        return max(dp)
