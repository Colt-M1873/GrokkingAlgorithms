# https://leetcode.com/problems/sort-colors/submissions/
# 2022年05月02日 14:37:17

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # v1 built in function
        # nums.sort()

        # # v2 bubble sort
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         if nums[i]>nums[j]:
        #             nums[i],nums[j]=nums[j],nums[i]
        
        # v3 copied three pointer swap
        p0=0
        p1=0
        p2=len(nums)-1
        while p1<=p2:
            if nums[p1]==0:
                nums[p1],nums[p0]=nums[p0],nums[p1]
                p0+=1
                p1+=1
            elif nums[p1]==2:
                nums[p1],nums[p2]=nums[p2],nums[p1]
                p2-=1
            else:
                p1+=1
                