# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
# 2022年05月06日 12:27:29

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # Functionality is more important than elegancy
        # v1 dumb sort, but superfast, why? 204ms, faster than 96.02%
        ns=sorted(nums)
        i=0
        j=len(nums)-1
        while i<len(nums):
            if nums[i]!=ns[i]:
                break
            else:
                i+=1
        while j>0:
            if nums[j]!=ns[j]:
                break
            else:
                j-=1
        if j==0:
            return 0
        return j-i+1