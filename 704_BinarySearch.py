# https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # # v1
        # lb=0 #lower boundary
        # hb=len(nums)-1
        # if target<nums[0] or target>nums[-1]:
        #     return -1
        # for i in range(len(nums)):
        #     half=(hb+lb)//2
        #     if nums[half]==target:
        #         return half
        #     elif nums[half]<target:
        #         lb=half
        #         if nums[half+1]>target:
        #             return -1
        #     elif nums[half]>target:
        #         hb=half
        #         if nums[half-1]<target:
        #             return -1

        # v2
        lb,hb=0,len(nums)-1
        while lb<=hb:
            pivot=(lb+hb)//2
            if nums[pivot]==target:
                return pivot
            if target<nums[pivot]:
                hb=pivot-1
            else:
                lb=pivot+1
        return -1