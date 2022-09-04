# https://leetcode.com/problems/numbers-with-same-consecutive-differences/
# 2022年09月03日 11:50:39

# v1 copied, slow
# https://leetcode.com/problems/numbers-with-same-consecutive-differences/discuss/798652/Python-simpleandclear-solution-wexpl-simpler-than-all-other-posts-I-saw!
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        init=list(i for i in range(1,10) if i+k<10 or i-k>-1)
        for lev in range(1,n):
            ret=[]
            for i in range(len(init)):
                if init[i]%10+k<10:
                    ret.append(init[i]*10+(init[i]%10+k))
                if 0<= init[i]%10-k <10:
                    ret.append(init[i]*10+(init[i]%10-k))
            init=ret[:]
        return list(set(ret))
                    
                