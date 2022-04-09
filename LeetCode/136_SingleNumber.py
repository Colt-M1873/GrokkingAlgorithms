# https://leetcode.com/problems/single-number/
# 2022年04月04日 18:40:25

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # # v1 too slow 9800ms    
        # s1=[]
        # for i in range(len(nums)):
        #     j=0
        #     l=len(s1)
        #     while j<l:
        #         if s1[j]==nums[i]:
        #             s1.pop(j)
        #             break
        #         j+=1
        #     if j==l:
        #         s1.append(nums[i])
        # return s1[0]

        # v2 bit manipulation, superfast 
        bitmask=nums[0]
        for item in nums[1:]:
            bitmask^=item # xor 
        return bitmask

        # v3 copied oneliner, bit manipulation using reduce() and lambda
        return reduce(lambda bitmask,item: bitmask^item, nums)
    
        # v3.1 oneliner super clean, bitmask using reduce() and builtin xor
        return reduce(xor,nums)
        