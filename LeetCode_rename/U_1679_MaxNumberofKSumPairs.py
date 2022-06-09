# https://leetcode.com/problems/max-number-of-k-sum-pairs/
# 2022年05月05日 10:15:27

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # Functionality is more important than elegance
        # v1 dumb with hash table, but not too slow, 820ms, faster than 56%
        ret=0
        d={}
        for i in range(len(nums)):
            if k-nums[i] in d:
                if d[k-nums[i]]>1:
                    d[k-nums[i]]-=1
                else:
                    d.pop(k-nums[i])
                ret+=1    
            else:
                if nums[i] not in d:
                    d[nums[i]]=1
                else:
                    d[nums[i]]+=1
        return ret
        
        