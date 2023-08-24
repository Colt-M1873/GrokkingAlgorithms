// https://leetcode.com/problems/search-in-rotated-sorted-array/description/
// 2023年08月24日 16:29:07

class Solution {
    public static int search(int[] nums, int target) {
        int pos=posBisect(nums);
        // System.out.println(pos);
        if(nums.length==1){
            if(nums[0]==target){
                return 0;
            }
            return -1;
        }
        int retpos;
        if(pos==-1){
            retpos = bisect(nums,0,nums.length-1,target);
        }else{
            if(target>=nums[0] && target<=nums[pos]){
                retpos = bisect(nums,0,pos,target);
            }else if(target>=nums[pos+1] && target<=nums[nums.length-1]){
                retpos = bisect(nums,pos+1,nums.length-1,target);
            }else{
                return -1;
            }
        }
        if(nums[retpos]==target){
            return retpos;
        }else{
            return -1;
        }

    }

    private static int posBisect(int[] nums){
        int l=0,r=nums.length-1;
        int mid=-1;
        while(l<r && nums[l]>nums[r]){
            mid=(l+r)/2;
            if(nums[l]>nums[r] && nums[mid]<nums[r]){
                r=mid;
            }else if(nums[l]>nums[r] && nums[mid]>nums[l]){
                l=mid+1;
            }else{
                return l;
            }
        }
        return mid;
    }

    private static int bisect(int[] nums,int low, int high, int target){
        int l=low,r=high;
        int mid=(l+r)/2;
        if(l==r){return l;}
        while(l<r){
            mid=(l+r)/2;
            if(nums[mid]>target){
                r=mid;
            }else if(nums[mid]<target){
                l=mid+1;
            }else{
                return mid;
            }
        }
        return l;
    }
}
