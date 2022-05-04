// https://leetcode.com/problems/summary-ranges/
// 2022年04月30日 21:33:29
import (
    "strconv"
)

func summaryRanges(nums []int) []string {
    var ret []string
    for i:=0;i<len(nums);i++{
        start:=nums[i]
        for i<len(nums)-1 && nums[i+1]-nums[i]==1 {
            i++
        }
        if start==nums[i] {
            ret=append(ret,strconv.Itoa(start))
        } else {
            ret=append(ret,strconv.Itoa(start)+"->"+strconv.Itoa(nums[i]))
        }
    }
    return ret
}