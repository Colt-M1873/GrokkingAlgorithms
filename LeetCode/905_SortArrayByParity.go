// https://leetcode.com/problems/sort-array-by-parity/
// 2022年05月02日 14:05:15

func sortArrayByParity(nums []int) []int {
    // v1 two pointer swap
    p1:=0
    p2:=len(nums)-1
    for p1<-p2 {
        if nums[p1]%2==1{
            nums[p1],nums[p2]=nums[p2],nums[p1]
            p2--
        }else{
            p1++
        }
    }
    return nums
}