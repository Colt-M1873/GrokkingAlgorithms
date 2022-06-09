# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# 2021 11.24

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # v1 Two Pointers
        left,right=0,len(numbers)-1
        while left<right:
            sums=numbers[left]+numbers[right]
            if sums>target:
                right-=1
            elif sums<target:
                left+=1
            else:
                return [left+1,right+1]