// https://leetcode.com/problems/binary-search/
// 2022年07月02日 10:24:07

import "fmt"
func search(nums []int, target int) int {
    l,h:=0,len(nums)-1
    for l<=h {
        mid:=(l+h)/2
        if nums[mid]<target {
            l=mid+1
        }else if nums[mid]>target{
            h=mid-1
        }else{
            return mid
        }
    } 
    return -1
}