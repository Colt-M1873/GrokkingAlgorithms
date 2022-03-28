# https://leetcode.com/problems/climbing-stairs/
# 2021 12.02


class Solution:
    def climbStairs(self, n: int) -> int:
        # # v1  
        # # total stair-steps n 
        # # need to walk wd walk-steps to finish
        # # each walk-step contains 1 or 2 stair-steps
        # # wd ranges from n to n//2+n%2 so 2-stair-steps ranges from 0 to n-(n//2+n%2) 
        # # i  denotes  2-stair-steps   so   i in range(0,n-(n//2+n%2)+1)
        # # for each wd contains a combination of cases
        # # that combination is to select all 2 stair-steps in wd, and wd = n-i
        # # that is C(i,wd) i.e. C(i,n-i)
        # # C(b,a)=a!/(b!*(a-b)!)
        # # C(3,5)=5!/(3!*(5-2)!)  
        # out=0 
        # for i in range(0,n-(n//2+n%2)+1):
        #     # calculate C(i,n-i)=(n-i)!/(i!*(n-i-i)!)
        #     combine=1
        #     # calculate (n-i)!/i!
        #     for j in range(i+1,n-i+1):
        #         combine*=j
        #     # (n-i)!/i!/(n-i-i)!
        #     for z in range(1,n-i-i+1):
        #         combine//=z
        #     out+=combine
        # return out

        # v2 copied  Recursion  clean and brilliant
        if n==2:
            return 2
        elif n==1:
            return 1
        else:
            return self.climbStairs(n-1)+self.climbStairs(n-2)

# s=Solution()
# print(s.climbStairs(9))

