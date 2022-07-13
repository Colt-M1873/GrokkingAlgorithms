# https://leetcode.com/problems/reverse-bits/
# 2022年04月19日 14:41:41
# 2022年07月13日 13:11:05

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # # v1 oneliner
        # # 变字符串，去掉0b，前补0到32位，翻转，变回int
        # return int((bin(n)[2:]).rjust(32,'0')[::-1],2)
        
        # v2 copied, bit manipulation
        ret=0
        for i in range(32):
            ret=(ret<<1) + (n&1)
            n>>=1
        return ret
    
        # # v3 oneliner, slow, adding every element
        # return sum(map(lambda x: ((n>>x)&1)<<(31-x), list(range(32))))
        
        # 2022年07月13日 12:40:18
        # v1
        ret=0
        for _ in range(32):
            ret=(ret|(n&1))<<1
            n>>=1
        return ret>>1
        
        # 2022年07月13日 12:55:51
        # v2
        return int(str(bin(n))[2:].zfill(32)[::-1],2)