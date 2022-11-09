// https://leetcode.com/problems/longest-increasing-subsequence
// 2022年11月09日 18:01:38

class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] dp = new int[nums.length]; // recort max subsequence length till now
        Arrays.fill(dp, 1);
        int ret = 1;
        for (int i = 1; i < nums.length; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
            ret = Math.max(ret, dp[i]);
        }
        return ret;
    }
}