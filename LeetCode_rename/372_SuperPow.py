# https://leetcode.com/problems/super-pow/
# 2021 12.07

class Solution:  
    def superPow(self, a: int, b: List[int]) -> int:
        # Important feature of pow and mod, modular exponentiation:
        #     (a*b)%k=(a%k)*(b%k)%k
        # Wiki about modular exponentiation:
        #     https://en.wikipedia.org/wiki/Modular_exponentiation
        # Binary Exponentiation
        
        # v1 copied oneliner using builtin pow(), pow has a mod parameter 
        return pow(a,int(''.join(str(x) for x in b)),1337)
        
        # # v2 copied  Modular Exponentiation and Binary Exponentiation
        # out=1
        # k=1337
        # for i in range(len(b)-1,-1,-1):
        #     a_b=self.binpow(a,b[i])
        #     for j in range(len(b)-i-1):
        #         a_b=self.binpow(a_b,10)
        #     out=(a_b%k)*(out%k)
        # return out%k
        
    # Python Binary Exponentiation
    def binpow(self,a, b):
        res = 1
        while b > 0:
            if (b & 1):
                res = res * a
            a = a * a
            b >>= 1
        return res