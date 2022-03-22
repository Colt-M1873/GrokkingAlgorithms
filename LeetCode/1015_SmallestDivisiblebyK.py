# https://leetcode.com/problems/smallest-integer-divisible-by-k/

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # https://en.wikipedia.org/wiki/Modular_arithmetic
        # https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/modular-addition-and-subtraction
        # (a+b)%k=(a%k+b%k)%k
        # (a*b)%k=((a%k)\*(b%k))%k

        # # v1 slow, 3626ms, onlu using mod plus feature: (a+b)%k=(a%k+b%k)%k
        # i=0
        # mod1=0
        # times10x=1
        # while i<k:
        #     mod10x=times10x%k
        #     mod1 = (mod1+mod10x)%k
        #     times10x*=10
        #     i+=1
        #     if mod1==0:
        #         return i
        #     if mod10x==0: # mod10x==0 means looping decimal
        #         return -1    
        # return -1
        
        # v2 faster 80ms, using mod plus and multiply feature:
        # (a+b)%k=(a%k+b%k)%k
        # (a*b)%k=((a%k)\*(b%k))%k
        i=0
        mod1=0
        mod10x=1
        while i<k:
            mod1 = (mod1+mod10x)%k
            mod10x=((mod10x%k)*(10%k))%k
            i+=1
            if mod1==0:
                return i
            if mod10x==0:
                return -1
        return -1    
        
            
            