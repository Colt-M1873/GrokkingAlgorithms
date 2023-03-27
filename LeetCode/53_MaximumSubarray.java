// https://leetcode.com/problems/maximum-subarray/
// 2023年03月04日 13:49:52
// still no idea

class Solution {
    public int maxSubArray(int[] nums) {
        int maxSum = nums[0];
        for (int i = 1; i < nums.length; i++) {
            nums[i] = Math.max(nums[i - 1] + nums[i], nums[i]);
            maxSum = Math.max(maxSum, nums[i]);
        }
        return maxSum;
    }
}