# https://leetcode.com/problems/contains-duplicate-ii/
# 2022年04月28日 11:58:14


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # # v1 right,but failed, too slow, pop and append cost too much time
        # array index is different from dictionary index
        # if k==0:
        #     return False
        # s=[]
        # i=0
        # while i<len(nums):
        #     if len(s)>=k:
        #         s.pop(0)
        #     if nums[i] not in s:
        #         s.append(nums[i])
        #     else:
        #         return True
        #     i+=1
        # return False
        
        # # v2 again too slow
        # if k == 0 or len(nums)==1:
        #     return False
        # if k>=len(nums):
        #     return len(set(nums))<len(nums)
        # l=0
        # r=min(k,len(nums))+1
        # while l<(len(nums)-k):
        #     # print(nums[l])
        #     # print(nums[l+1:r])
        #     if nums[l] in nums[l+1:r]:
        #         return True
        #     l+=1
        #     r+=1
        # # print(l,r)
        # # print(nums[l-1:r])
        # return len(set(nums[l-1:r]))<(r-l)
        
        # v3 passed,1333ms,dict index is way faster
        if k==0:
            return False
        d={}
        i=0
        while i<len(nums):
            # print(nums[i])
            # print(d)
            if nums[i] not in d.keys():
                d[nums[i]]=True
            else:
                return True
            if len(d)>k:
                # print("i-k",nums[i-k])
                d.pop(nums[i-k])
            
            i+=1
        return False