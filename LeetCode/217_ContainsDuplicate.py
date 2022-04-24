# https://leetcode.com/problems/contains-duplicate/
# 2022年04月24日 20:22:11

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # v1 oneliner
        return len(set(nums))<len(nums)
        