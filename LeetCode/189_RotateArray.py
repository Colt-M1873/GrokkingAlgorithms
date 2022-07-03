# https://leetcode.com/problems/rotate-array/
# 2022年07月02日 22:11:01

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # v1 slow, 2324ms
        # k=k%len(nums)
        # while k>0:
        #     k-=1
        #     nums.insert(0,nums.pop()) 
        
        # v2 slice assignment, 300ms
        k%=len(nums)
        nums[:]=nums[-k:]+nums[:-k] 
        