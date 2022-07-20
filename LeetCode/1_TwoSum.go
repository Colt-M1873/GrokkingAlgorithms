// https://leetcode.com/problems/two-sum/
// 2022年07月19日 17:35:44

func twoSum(nums []int, target int) []int {
    m := make(map[int]int) // create empty map
    for i:=0; i<len(nums); i++ {
        if val,ok:=m[nums[i]]; ok{ // see if val in map
            return []int{i,val}
        }else{
            m[target-nums[i]]=i
        }
    }
    return []int{0,0}
}