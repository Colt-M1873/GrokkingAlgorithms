# https://leetcode.com/problems/sort-array-by-parity/
# 2022年05月02日 13:51:45

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # # v1 two pointer swap
        # slow=0
        # fast=len(nums)-1
        # while slow<=fast:
        #     if nums[slow]%2==1 and nums[fast]%2==0:
        #         nums[slow],nums[fast]=nums[fast],nums[slow]
        #         slow+=1
        #         fast-=1
        #     elif nums[slow]%2==0:
        #         slow+=1
        #     elif nums[fast]%2==1:
        #         fast-=1
        # return nums
        
        # # v1.1 two pointer swap improved, more concise and clear
        # p1=0
        # p2=len(nums)-1
        # while p1<p2:
        #     if nums[p1]%2==1:
        #         nums[p1],nums[p2]=nums[p2],nums[p1]
        #         p2-=1
        #     else:
        #         p1+=1
        # return nums
          
        # # v2 copied oneliner
        # return sorted(nums,key=lambda x: x%2)
        
        # v2.1 copied oneliner, bit manipulation
        return sorted(nums,key=lambda x : x&1)