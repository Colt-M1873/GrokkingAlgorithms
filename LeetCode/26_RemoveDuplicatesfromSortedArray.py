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
        
<<<<<<< HEAD:26_RemoveDuplicatesfromSortedArray.py
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
=======
        # v2 two pointers
        a,b=0,0
        while b<len(nums):
            if nums[b]==nums[a]:
                b+=1
            elif nums[b]>nums[a]:
                a+=1
                nums[a],nums[b]=nums[b],nums[a]
                b+=1
        a+=1
        return a

>>>>>>> 9ad0438a3efe2444c740cdab89d8ac48145c6cb4:LeetCode/26_RemoveDuplicatesfromSortedArray.py

        # v3 copied  using slice assignment '[:]' elegant in-place operation
        nums[:] = sorted(set(nums))
        # return len(nums) 