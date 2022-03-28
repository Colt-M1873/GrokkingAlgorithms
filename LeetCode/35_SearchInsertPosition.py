# https://leetcode.com/problems/search-insert-position/submissions/
# 2021 11.20

class Solution:
    
    # # v0 zeroliner, like v4 but just replaced the function name with builtin function, bravo
    # searchInsert = bisect.bisect_left
    
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # # v1
        # left, right = 0, len(nums)-1
        # if target<nums[0]:
        #     return 0
        # elif target>nums[-1]:
        #     return len(nums)
        # while left <= right:
        #     pivot = (left+right)//2
        #     if nums[pivot] < target:
        #         left = pivot+1
        #         if nums[left]>target:
        #             return left
        #     elif nums[pivot] == target:
        #         return pivot
        #     elif nums[pivot] > target:
        #         right = pivot-1
        #         if nums[right]<target:
        #             return pivot
        
        
        # v1.1 copied  OG binary search with O(logn),removed excess comparements
        left, right = 0, len(nums)-1
        while left <= right:
            pivot = (left+right)//2
            if nums[pivot] < target:
                left = pivot+1
            elif nums[pivot] == target:
                return pivot
            elif nums[pivot] > target:
                right = pivot-1
        return left
        
        
        # # v2 copied  linear search with a complexity of O(n), not binary
        # for i in nums:
        #     if i >= target:
        #         return nums.index(i)
        # return len(nums)
        
        
        # # v3 copied  oneliner sort new list and get index
        # return sorted(nums + [target]).index(target)
    
    
        # # v4 copied  oneliner builtin binary search module
        # return bisect.bisect_left(nums,target)
    
    
        # # v5 copied oneliner O(n) method, not very fast
        # return len([x for x in nums if x<target])
        