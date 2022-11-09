// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
// 2022年11月09日 14:34:18

// v1 Oct 30, 2022 22:45
class Solution {
    public int maxProfit(int[] prices) {
        // real DP
        int ret = 0;
        for (int i = 1; i < prices.length; i++) {
            ret += Math.max(0, prices[i] - prices[i - 1]);
        }
        return ret;
    }
}

// v2
class Solution {
    public int maxProfit(int[] prices) {
        int ret = 0;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] > prices[i - 1]) {
                ret += prices[i] - prices[i - 1];
            }
        }
        return ret;
    }
}