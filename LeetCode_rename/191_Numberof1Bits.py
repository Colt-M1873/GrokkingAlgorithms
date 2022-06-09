# https://leetcode.com/problems/number-of-1-bits/
# 2022年04月19日 13:20:46

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # # v1 bit move
        # ret=0
        # for i in range(32):
        #     ret+=n&1
        #     n=n>>1
        # return ret
    
        # #v1.1 oneliner
        return sum(map(lambda x: (n>>x)&1,list(range(0,32))))
    
        # # v2 copied onelienr
        # return bin(n).count('1')
    
        # v3 copied 
        # https://leetcode.com/problems/number-of-1-bits/discuss/1044775/Python-n-and-(n-1)-trick-%2B-even-faster-explained
        # Worth mentioning that this solution will only loop as many times as the number of 1 bits whereas the solutions shifting the bits of n will loop also for every 0 bit in between.
        ans=0
        while n:
            n &= (n-1)
            ans += 1
        return ans