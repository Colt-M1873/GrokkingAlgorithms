# https://leetcode.cn/problems/special-array-with-x-elements-greater-than-or-equal-x/
# 2022年09月12日 22:17:03

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        nums.append(-1)
        for idx in range(len(nums)):
            if nums[idx]>=idx+1 and nums[idx+1]<idx+1:
                return idx+1
            if nums[idx]<idx+1:
                return -1
        return -1