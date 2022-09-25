// https://leetcode.com/problems/two-sum/
// 2022年09月22日 14:56:04

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> d=new HashMap<>();
        for (int i=0;i<nums.length;i++){
            if (d.get(nums[i])!=null){
                return (new int[] {i,d.get(nums[i])});
            }
            d.put(target-nums[i],i);
        }
        return (new int[2]);
    }
}

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> d=new HashMap<>();
        for (int i=0;i<nums.length;i++){
            if (d.containsKey(nums[i])){
                return (new int[] {i,d.get(nums[i])});
            }
            d.put(target-nums[i],i);
        }
        return (new int[2]);
    }
}