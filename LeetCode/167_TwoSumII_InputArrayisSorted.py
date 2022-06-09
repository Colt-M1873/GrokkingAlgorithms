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

        # # v2 hash table the same as problem No.1
        # # passed but not constant space?
        # d={}
        # for idx,item in enumerate(numbers):
        #     if item not in d:
        #         d[target-item]=idx
        #     else:
        #         return [d[item]+1,idx+1]

        # v3 two pointer with binary search
        for i in range(len(numbers)):
            l, r = i+1, len(numbers)-1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r-l)//2
                if numbers[mid] == tmp:
                    return [i+1, mid+1]
                elif numbers[mid] < tmp:
                    l = mid+1
                else:
                    r = mid-1