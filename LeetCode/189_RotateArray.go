// https://leetcode.com/problems/rotate-array/
// 2022年07月03日 20:30:03

func rotate(nums []int, k int)  {
    nk:=len(nums)-k%len(nums)
    // copy means copies elements into a certain destination slice from a source slice, is an in-place operation 
    copy(nums,append(nums[nk:],nums[:nk]...))
    // directly assign is not in-place 
    // nums=append(nums[nk:],nums[:nk]...)
}

