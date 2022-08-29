// https://leetcode.cn/problems/shuffle-the-array/submissions/
// 2022年08月29日 10:40:24
func shuffle(nums []int, n int) []int {
    ret:=[]int{}
    for i:=0;i<n;i++{
        ret=append(ret,nums[i],nums[n+i])
    }
    return ret
}