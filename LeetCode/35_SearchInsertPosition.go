// https://leetcode.com/problems/search-insert-position/submissions/
// 2022年07月02日 10:54:53

func searchInsert(nums []int, target int) int {
    l,h:=0,len(nums)-1
    for l<=h {
        mid := (l+h)/2
        if nums[mid]<target {
            l=mid+1
        }else if nums[mid]>target {
            h=mid-1
        }else{
            return mid
        }   
    }
    return l
}