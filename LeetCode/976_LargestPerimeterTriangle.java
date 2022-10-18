// https://leetcode.com/problems/largest-perimeter-triangle/
// 2022年10月12日 11:58:46

class Solution {
    public int largestPerimeter(int[] nums) {
        // 直接排序后由大向小找就可以，因为不存在那种nums[i]>nums[i-1]+nums[i-2]但是nums[i]<nums[i-2]+nums[i-3]的情况
        Arrays.sort(nums);
        for (int i=nums.length-1;i>=2;i--){
            if(nums[i]+nums[i-1]>nums[i-2]&&nums[i]+nums[i-2]>nums[i-1]&&nums[i-2]+nums[i-1]>nums[i]){
                return nums[i]+nums[i-1]+nums[i-2];
            }
            // System.out.println(nums[i]);
        }
    return 0;    
    }
}