// https://leetcode.com/problems/contains-duplicate-ii/submissions/
// 2022年04月28日 18:17:00

func containsNearbyDuplicate(nums []int, k int) bool {
    d:=make(map[int]int)
    for i:=0;i<len(nums);i++{
        if _,ok := d[nums[i]]; ok{
            return true
        }
        d[nums[i]]=1
        if len(d)>k{
            delete(d,nums[i-k])
        }
    }
	return false
}