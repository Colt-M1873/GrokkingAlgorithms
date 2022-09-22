# https://leetcode.com/problems/sum-of-even-numbers-after-queries/
# 2022年09月22日 11:58:14

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # orig sum of even numbers
        ret=[]
        es=0 # even sum
        for n in nums:
            if n%2==0:
                es+=n
        # print(es)
        for q in queries:
            orign=nums[q[1]]
            nums[q[1]]=orign+q[0] # newn n+q[0]
            if orign%2==1: # if orig num n is odd
                if nums[q[1]]%2==0: # new n is even
                    es=es+nums[q[1]] # then add newn, if orign and newn are all odd, then ignore
            else: # if orig n is even
                if nums[q[1]]%2==0: # new n is also even
                    es=es+q[0] # add the difference between orig and new
                else:
                    es=es-orign # if new n is odd, then detract original n
            ret.append(es)
        return ret
            
            