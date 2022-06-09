# https://leetcode.com/problems/partition-equal-subset-sum/
# 2021 12.12

# Knapsack(Backpack) prblems, guide:
# https://leetcode.com/discuss/study-guide/1200320/Thief-with-a-knapsack-a-series-of-crimes.

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        for sublen in range(1,len(nums)//2+1):
            subset=[0]*sublen
            for subitemindex in range(sublen):

                subset[subitemindex]=nums[]




                # for i in range(subitemindex,sublen+1):
                #     subset.append(nums[i])
                