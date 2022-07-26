// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
// 2022年07月25日 12:58:46

func searchRange(nums []int, target int) []int {
    start,end:=-1,-1
    for i:=0;i<len(nums);i++ {
        if nums[i]==target && start==-1 {
            start=i
        }
        if start!=-1 && end==-1 && nums[i]!=target{
            end=i-1
        }
    }
    if start!=-1 && end==-1{
        end=len(nums)-1
    }
    return []int{start,end}
}