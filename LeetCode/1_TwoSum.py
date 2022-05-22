# https://leetcode.com/problems/two-sum/
# 2021 11.20 

def twoSum(nums: list[int], target: int) -> list[int]:
    # v1 3644ms
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

    # v3 copied 70ms
    hashmap={}
    for i in range(len(nums)):
        hashmap[nums[i]]=i
        complement=target-nums[i]
        if complement in hashmap:
            return[i,hashmap[complement]]

    # 2022年05月20日 11:03:41 
    # using hash table  70ms
    d={}
    for idx, item in enumerate(nums):
        if item not in d:
            d[target-item]=idx
        else:
            return [d[item],idx]


a=[1,2,3,5,8,6,5]
print(twoSum(a,8))