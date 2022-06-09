# https://leetcode.com/problems/sqrtx/
# 2021 12.01

class Solution:
    def mySqrt(self, x: int) -> int:
        # v1 oneliner  20ms  faster than 99%
        return int(sqrt(x))
        
        # # v2  whole for, really slow, 7168ms
        # for i in range(x+1):
        #     if (i+1)**2>x:
        #         return i
        
        # # v3 Binary search 40ms
        # l,r=0,x
        # while l<=r:
        #     pivot=int(0.5*(l+r))
        #     p=pivot**2
        #     if p==x:
        #         return int(pivot)
        #     elif p<x:
        #         if (pivot+1)**2>x:
        #             return pivot 
        #         l=pivot+1
        #     else:
        #         r=pivot-1