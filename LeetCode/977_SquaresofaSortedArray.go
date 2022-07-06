// https://leetcode.com/problems/squares-of-a-sorted-array/
// 2022年07月05日 11:52:46

func sortedSquares(nums []int) []int {
    // append a variable to a slice is way faster than appending two slices or arrays
    
    // // v1 slow, 1343ms
    // l,r :=0,len(nums)-1
    // ret := []int{}
    // for l<=r {
    //     if -nums[l]>nums[r] {
    //         ret=append([]int{nums[l]*nums[l]},ret...) 
    //         l++
    //     } else{
    //         ret=append([]int{nums[r]*nums[r]},ret...) 
    //         r--
    //     }
    // }
    // return ret
    
    // 2022年07月05日 21:20:00
    // v2 faster, 55ms
    l,r :=0,len(nums)-1
    ret := []int{}
    for l<=r {
        if -nums[l]>nums[r] {
            ret=append(ret,nums[l]*nums[l]) 
            l++
        } else{
            ret=append(ret,nums[r]*nums[r])
            r--
        }
    }
    for a,b:=0,len(nums)-1;a<b;a,b=a+1,b-1{
        ret[a],ret[b]=ret[b],ret[a]
    }
    return ret
}