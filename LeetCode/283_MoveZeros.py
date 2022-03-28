# https://leetcode.com/problems/move-zeroes/submissions/
# 2021 11.23

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # v1  commom dumb iteration
        # a=nums
        # i=0
        # n=0
        # while i < len(a)-n:
        #     if a[i]==0:
        #         a.pop(i)
        #         a.append(0)
        #         n+=1
        #     else:
        #         i+=1
                
        # # v2 copied  oneliner but a little confusing 
        # nums.sort(key= lambda x: 1 if x == 0 else 0)
        
        # # v2.1 copied  elegant oneliner
        # nums.sort(key=bool, reverse=True)
        
        
        # v3 copied  elegant two pointer
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 :
                nums[slow], nums[fast] = nums[fast], nums[slow]
            # wait until fast find a non-zero element to swap with slow
                slow += 1