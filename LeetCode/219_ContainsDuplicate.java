// https://leetcode.com/problems/contains-duplicate-ii/submissions/
// 2022年10月21日 13:48:19

class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        HashMap<Integer,Integer> h=new HashMap<>();
        for(int i=0;i<nums.length;i++){
            // System.out.println(h.get(0));
            if(h.get(nums[i])!=null){
                return true;
            }
            h.put(nums[i],-1);
            if(h.size()>k){
                h.remove(nums[i-k]);
            }
        }
    return false;
    }
}