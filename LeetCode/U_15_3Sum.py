# https://leetcode.com/problems/3sum/
# 2022年07月16日 10:48:58

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # v1 slow using set
        # list is not hashabel, so list can't be element of set, but tuples can
        ret=set() # using set to avoid duplicate
        nums=sorted(nums)
        # print(nums)
        for i in range(len(nums)):
            currSum=-nums[i]
            d={}
            for j in range(i+1,len(nums)):
                if nums[j] in d:
                    ret.add((nums[i],d[nums[j]],nums[j])) # list is unhashabel but tuple is hashable
                else:
                    d[currSum-nums[j]]=nums[j]
        return ret