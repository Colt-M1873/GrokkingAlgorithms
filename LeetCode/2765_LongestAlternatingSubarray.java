// https://leetcode.com/problems/longest-alternating-subarray/

class Solution {
    public int alternatingSubarray(int[] nums) {
        int m=-1;
        int curr=1;
        for(int i=1;i<nums.length;i++){
            if(Math.abs(nums[i]-nums[i-1])==1){
                if(nums[i]-nums[i-1]==-1 && curr==1){
                    continue;
                }
                curr++;
                if(i>1 && nums[i]!=nums[i-2]){
                    curr=2;
                }
                m=Math.max(curr,m);
            }else{
                curr=1;
            }
        }
        return m;
    }
}
