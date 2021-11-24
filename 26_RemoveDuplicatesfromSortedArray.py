# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # # v1 common
        # i=0
        # while i<len(nums)-1:
        #     if nums[i]==nums[i+1]:
        #         nums.pop(i)
        #     else:
        #         i+=1
        
        # v2 two pointers



        # v3 copied  using slice assignment '[:]' elegant in-place operation
        nums[:] = sorted(set(nums))
        # return len(nums) 