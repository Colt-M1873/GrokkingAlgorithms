// https://leetcode.cn/problems/min-cost-climbing-stairs/
// 2022年10月22日 11:41:34

class Solution {
    public int minCostClimbingStairs(int[] cost) {
        for (int i = 2; i < cost.length; i++) {
            cost[i] += Math.min(cost[i - 1], cost[i - 2]);
        }
        return Math.min(cost[cost.length - 1], cost[cost.length - 2]);
    }
}

// 2023年03月02日 14:33:30
class Solution {
    public int minCostClimbingStairs(int[] cost) {
        if (cost.length == 2) {
            return Math.min(cost[0], cost[1]);
        }
        int L = cost.length;
        for (int i = 2; i < L; i++) {
            cost[i] += Math.min(cost[i - 1], cost[i - 2]);
        }
        return Math.min(cost[L - 1], cost[L - 2]);
    }
}