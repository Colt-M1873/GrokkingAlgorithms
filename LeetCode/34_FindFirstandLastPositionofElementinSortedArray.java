// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
// 2023年08月24日 17:06:30

class Solution {
    public int[] searchRange(int[] nums, int target) {
        if(nums.length==0){return new int[]{-1,-1};}
        int l=0,r=nums.length-1;
        int mid=0;
        int retpos=-1;
        while(l<r){
            mid=(l+r)/2;
            if(nums[mid]>=target){
                r=mid;
            }else{
                l=mid+1;
            }
        }
        retpos=l;
        if(nums[l]!=target){
            return new int[]{-1,-1};
        }

        
        int newl=0,start=l,end=l,newr=nums.length-1;
        while(newl<start){
            int newmid=(newl+start)/2;
            if(nums[newmid]<target){
                if(nums[newmid+1]==target){
                    start=newmid+1;
                    break;
                }
                newl=newmid+1;
            }else{
                start=newmid;
            }
        }
        while(end<newr){
            int newmid=(end+newr)/2;
            if(nums[newmid]>target){
                if(nums[newmid-1]==target){
                    end=newmid-1;
                    break;
                }
                newr=newmid-1;
            }else{
                if(nums[newmid+1]!=target){
                    end=newmid;
                    break;
                }
                end=newmid+1;
            }
        }
        return new int[]{start,end};
    }
}
