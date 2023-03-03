// https://leetcode.com/problems/jump-game-ii/description/
// 2023年03月03日 11:26:57

class Solution {
    public int jump(int[] nums) {
        // use another dp array recording least steps till current spot, and iteratively
        // minimize each value
        int[] dp = new int[nums.length];
        Arrays.fill(dp, nums.length);
        dp[0] = 0;
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j <= nums[i]; j++) {
                if (i + j < nums.length) {
                    dp[i + j] = Math.min(dp[i + j], dp[i] + 1);
                }
            }
        }
        // for (int num: dp){
        // System.out.print(num+",");
        // }
        return dp[nums.length - 1];
    }
}