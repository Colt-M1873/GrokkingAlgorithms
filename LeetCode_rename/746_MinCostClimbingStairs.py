# https://leetcode.com/problems/min-cost-climbing-stairs/
# 2022年06月07日 11:37:08

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # # v1 dp
        # dp就是简化问题，找局部的子问题，从中间的某一环去看他的先后关系，也就是找递推公式，然后看它的起始和终止条件
        # 物有本末，事有终始，知其先后，则近道矣
        # # dp记录total cost，分为两种情况？记录每种情况里最小的cost？
        # # 和70-爬楼梯一样，找合理的递推公式
        # # 在这道题里从底层到第i级台阶的花费=第i级的花费 + （第i-1和第i-2级台阶花费中的最小值）
        # # 即 total(i) = cost(i) + min(total(i-1),total(i-2))
        # dp=[0]*len(cost)
        # dp[:2] = cost[:2] # 起始条件
        # for i in range(2,len(cost)):
        #     dp[i]=cost[i]+min(dp[i-1],dp[i-2]) # 递推公式
        # return min(dp[-1],dp[-2])
        
        # v1.1 dp with less space cost
        for i in range(2,len(cost)):
            cost[i]+=min(cost[i-1],cost[i-2])
        return min(cost[-1],cost[-2])

        # DP的仔细拆解分析
        # https://leetcode.com/problems/min-cost-climbing-stairs/discuss/476388/4-ways-or-Step-by-step-from-Recursion-greater-top-down-DP-greater-bottom-up-DP-greater-fine-tuning