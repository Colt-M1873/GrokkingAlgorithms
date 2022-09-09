# https://leetcode.cn/problems/beautiful-arrangement/
# 2022年09月08日 14:09:13

class Solution:
    def countArrangement(self, n: int) -> int:
        # copied, binary status compression and dynamic programming
        # https://leetcode.cn/problems/beautiful-arrangement/solution/you-mei-de-pai-lie-by-leetcode-solution-vea2/
        dp=[0]*(1<<n)
        dp[0]=1
        for mask in range(1,1<<n): # mask iterates through all choosing conditions
            nth = bin(mask).count('1')
            for i in range(n):
                if mask & (1<<i) and  ((nth%(i+1))==0 or ((i+1)%nth)==0 ): 
                    # mask & (1<<i) == True denotes the i th place is chosen
                    # (nth%i)==0 or (1%nth)==0 are the conditions requested in problem
                    dp[mask]+=dp[mask^(1<<i)]
        # print(dp)
        return dp[-1]