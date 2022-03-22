# https://leetcode.com/problems/remove-element/submissions/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # # v1  common pop
        # i=0
        # while i<len(nums):
        #     if nums[i] == val:
        #         nums.pop(i)
        #     else:
        #         i+=1
        # return i

        # v2 two pointer
        i,j=0,len(nums)-1
        while i<=j:
            if nums[i]==val:
                nums[i], nums[j], j = nums[j], nums[i], j-1
            else:
                i+=1
        return i
