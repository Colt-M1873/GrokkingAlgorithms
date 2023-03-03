// https://leetcode.com/problems/house-robber-ii/description/?envType=study-plan&id=dynamic-programming-i
// 2023年03月03日 10:22:59

class Solution {
    public int rob(int[] nums) {
        if(nums.length==1){return nums[0];}
        int[] a=Arrays.copyOf(nums,nums.length-1);
        int[] b = new int[nums.length-1];
        System.arraycopy(nums,1,b,0,nums.length-1);
        return Math.max(this.rob1(a),this.rob1(b));
    }

    public int rob1(int[] nums){
        if(nums.length==1){return nums[0];}
        nums[1]=Math.max(nums[0],nums[1]);
        for(int i=2;i<nums.length;i++){
            nums[i]=Math.max(nums[i-2]+nums[i],nums[i-1]);
        }
        return Math.max(nums[nums.length-2],nums[nums.length-1]);
    }
}