# https://leetcode.com/problems/two-sum/
# 2021 11.20 

def twoSum(nums: list[int], target: int) -> list[int]:
    # v1
    # len1=len(nums)
    # for i in range(0,len1):
    #     num1=nums.pop(0)
    #     for idx,item in enumerate(nums):
    #         if num1+item==target:
    #             return [i, idx+i+1]
    
    # v2
    # len1=len(nums)
    # for i in range(0,len1):
    #     for j in range(i+1,len1):
    #         if nums[i]+nums[j]==target:
    #             return [i, j]

    # v3 copied
    hashmap={}
    for i in range(len(nums)):
        hashmap[nums[i]]=i
        complement=target-nums[i]
        if complement in hashmap:
            return[i,hashmap[complement]]

a=[1,2,3,5,8,6,5]
print(twoSum(a,8))