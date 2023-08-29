// https://leetcode.com/problems/house-robber/
// 2022年12月14日 11:28:54

// // O(n) time O(n) space
// class Solution {
//     public int rob(int[] nums) {
//         if (nums.length < 2) {
//             return nums[0];
//         }
//         int[] dp = new int[nums.length]; // recording current max
//         dp[0] = nums[0];
//         dp[1] = Math.max(nums[0], nums[1]);

//         for (int i = 2; i < nums.length; i++) {
//             dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i]);
//         }
//         return dp[nums.length - 1];
//     }
// }

// O(n) time O(1) space
class Solution {
    public int rob(int[] nums) {
        if (nums.length < 2) {
            return nums[0];
        }
        int lastMax_1 = Math.max(nums[0], nums[1]);
        int lastMax_2 = nums[0];
        int ret = lastMax_1;
        for (int i = 2; i < nums.length; i++) {
            ret = Math.max(lastMax_2 + nums[i], lastMax_1);
            lastMax_2 = lastMax_1;
            lastMax_1 = ret;
        }
        return ret;
    }
}

// 2023年03月02日 14:40:12
class Solution {
    public int rob(int[] nums) {
        if (nums.length == 1) {
            return nums[0];
        }
        nums[1] = Math.max(nums[1], nums[0]);
        for (int i = 2; i < nums.length; i++) {
            nums[i] = Math.max(nums[i] + nums[i - 2], nums[i - 1]);
        }
        return Math.max(nums[nums.length - 1], nums[nums.length - 2]);
    }
}


// 2023年08月29日 10:12:26
class Solution {
    public int rob(int[] nums) {
        if(nums.length==1){return nums[0];}
        nums[1]=Math.max(nums[0],nums[1]);
        for(int i=2;i<nums.length;i++){
            nums[i]=Math.max(nums[i-2]+nums[i],nums[i-1]);
        }
        return nums[nums.length-1];
    }
}








