# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# 2021 12.06 2022 3.15


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # # v1 common
        # i=0
        # while i<len(nums)-1:
        #     if nums[i]==nums[i+1]:
        #         nums.pop(i)
        #     else:
        #         i+=1
        
        # # v2 two pointers 2022 3.15
        # while b<len(nums):
        #     if nums[b]==nums[a]:
        #         b+=1
        #     elif nums[b]>nums[a]:
        #         a+=1
        #         nums[a],nums[b]=nums[b],nums[a]
        #         b+=1
        # a+=1
        # return a

        # v3 copied  using slice assignment '[:]' elegant in-place operation
        nums[:] = sorted(set(nums))
        # return len(nums) 