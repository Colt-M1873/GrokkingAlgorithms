//https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
// 2022年11月09日 16:00:59

class Solution {
    public int maxProfit(int[] prices, int fee) {
        // dp表示当天的现金，dp[i][0]表示持有，dp[i][1]表示不持有，只有这两种状态
        // 状态的转移发生在：
        // 1 由持有到不持有，即dp[i][1]=dp[i-1][0]+prices[i]-fee; 或者保持持有，即dp[i][1]=dp[i-1][1]
        // 2 由不持有到持有，即dp[i][0]=dp[i-1][1]-prices[i]; 或者保持不持有，即dp[i][0]=dp[i-1][0]
        // 初始状态为 买入，即dp[0][0]=-prices[0] 和 不买入，即dp[0][1]=0
        int[][] dp = new int[prices.length][2];
        dp[0][0] = -prices[0];
        for (int i = 1; i < prices.length; i++) {
            dp[i][0] = Math.max(dp[i - 1][0], dp[i - 1][1] - prices[i]);
            dp[i][1] = Math.max(dp[i - 1][1], dp[i - 1][0] + prices[i] - fee);
        }
        return dp[prices.length - 1][1];
    }
}