# https://leetcode.com/problems/summary-ranges/
# 2022年04月30日 21:05:43

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # # v1 common one pass
        # ret=[]
        # i=0
        # while i<len(nums):
        #     start=end=nums[i]
        #     while i<len(nums)-1 and nums[i+1]-nums[i]==1:
        #         i+=1
        #     end=nums[i]
        #     i+=1
        #     if start==end:
        #         ret.append(str(start))
        #     else:
        #         ret.append(str(start)+'->'+str(end))
        # return ret
        
        # v1.1 removed end variable
        ret=[]
        i=0
        while i<len(nums):
            start=nums[i]
            while i<len(nums)-1 and nums[i+1]-nums[i]==1:
                i+=1
            if start==nums[i]:
                ret.append(str(start))
            else:
                ret.append(str(start)+'->'+str(nums[i]))
            i+=1
        return ret