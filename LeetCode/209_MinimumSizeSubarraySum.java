// https://leetcode.com/problems/minimum-size-subarray-sum/description/

// 2023年08月31日 16:45:31
class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int l=0,r=0;
        int sum=0;
        int ret=nums.length+1;
        while(r<nums.length){
            sum+=nums[r];
            r++;
            while(sum>=target){
                ret=Math.min(ret,r-l);
                sum-=nums[l];
                l++;
            }
        }
        if(ret==nums.length+1){
            return 0;
        }
        return ret;
    }
}
