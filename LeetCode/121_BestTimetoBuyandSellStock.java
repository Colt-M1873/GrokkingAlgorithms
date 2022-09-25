// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/
// 2022年09月22日 14:37:03

// 7ms
class Solution {
    public int maxProfit(int[] prices) {
        int[] dp=new int[prices.length];
        int currMin=prices[0];
        for (int i=0;i<prices.length;i++){
            if (prices[i]<currMin){
                currMin=prices[i];
            }
            dp[i]=prices[i]-currMin;
        }
        int ret = Arrays.stream(dp).max().getAsInt();
        return ret;
    }
}

// 1ms
class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit=0,currMin=prices[0];
        for (int i=0;i<prices.length;i++){
            if (prices[i]<currMin){
                currMin=prices[i];
            }
            maxProfit=Math.max(maxProfit,prices[i]-currMin);
        }
        return maxProfit;
    }
}