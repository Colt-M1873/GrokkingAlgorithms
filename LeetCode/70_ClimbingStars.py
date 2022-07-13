# https://leetcode.com/problems/climbing-stairs/
# 2021 12.02
# 2022年06月07日 
# 2022年07月12日 13:57:07

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

        # # v2 copied  Recursion, TLE  clean and brilliant， but TLE
        # if n==2:
        #     return 2
        # elif n==1:
        #     return 1
        # else:
        #     return self.climbStairs(n-1)+self.climbStairs(n-2)


        # 2022年06月07日 11:07:58
        # dp
        # 找递推公式，因为每次只能走一格或者两格，所以第i级只能通过第i-1级走1格和第i-2级走2格达成，
        # 因此第i级的走法就是第i-1和i-2级走法的和
        # dp=[0]*(n+1)
        # dp[1]=1
        # if n>1:
        #     dp[2]=2
        # for i in range(3,n+1):
        #     dp[i]=dp[i-1]+dp[i-2]
        # return dp[n]
        
        # # v2 
        # # 上一版本的dp数组里只有最后两项有用，因此可以用两个变量而非一整个数组来存储
        # # 节省了一丢丢数组的空间，空间复杂度从O(n)变成了O(1) ?应该是吧
        # if n<3: return n
        # dpi_1=2
        # dpi_2=1
        # for _ in range(2,n):
        #     dpi=dpi_1+dpi_2
        #     dpi_2=dpi_1
        #     dpi_1=dpi
        # return dpi        

        # # 再简化
        # # v3 copied https://leetcode.com/problems/climbing-stairs/discuss/25296/3-4-short-lines-in-every-language
        # a = b = 1
        # for _ in range(n):
        #     a, b = b, a + b
        # return a


        # ultimate, 2022年07月12日 13:56:12
        # DP list, like recursive but superfast
        dp=[0,1,2] # dp[1]=1, dp[2]=2
        if n<=2: return dp[n]
        while n>2:
            dp.append(dp[-1]+dp[-2])
            n-=1
        return dp[-1]
        


        # 2022年07月13日 11:57:17
        # ultimate+
        dp=[0,1,2] # dp[1]=1 dp[2]=2
        for _ in range(2,n):
            dp.append(dp[-1]+dp[-2])
        return dp[n]