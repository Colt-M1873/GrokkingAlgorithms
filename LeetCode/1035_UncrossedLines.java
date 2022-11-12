// https://leetcode.com/problems/uncrossed-lines/description/
// 2022年11月11日 18:08:55

class Solution {
    public int maxUncrossedLines(int[] nums1, int[] nums2) {
        // 二维dp数组记录从前向后的可能的线的条数
        // dp[i][j]：长度为[0, i - 1]的字符串text1与长度为[0, j - 1]的字符串text2的最长公共子序列为dp[i][j]
        // 二维DP从左上向右下推进，可能有三个方向，即向下，向右，向右下
        // 当二者相等时候向右下推进
        // 当不相等时候，比较二者的最大值决定是选择上方还是右方
        int ret=0;
        int[][] dp= new int[nums1.length+1][nums2.length+1];
        for(int i=1;i<nums1.length+1;i++){
            for(int j=1;j<nums2.length+1;j++){
                if(nums1[i-1]==nums2[j-1]){
                    dp[i][j]=dp[i-1][j-1]+1;
                }else{
                    dp[i][j]=Math.max(dp[i-1][j],dp[i][j-1]);
                }
            }
        }
        // for(int[] row:dp){
        //     for(int r:row){
        //         System.out.print(r+",");
        //     }
        //     System.out.println();
        // }
        return dp[nums1.length][nums2.length];
    }
}