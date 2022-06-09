// https://leetcode.com/problems/contains-duplicate/submissions/
// 2022年04月24日 21:22:38
func containsDuplicate(nums []int) bool {
    // v1
    // var set = []int{nums[0]}
    // for i:=1;i<len(nums);i++ {
    //     for j:=0;j<len(set);j++{
    //         if nums[i]==set[j]{
    //             return true
    //         }
    //     }
    //     set=append(set,nums[i])
    // }
    // return false
    
    // // v2 classic brutal slow 1465ms
    // var tmp int
    // for i:=0;i<len(nums);i++ {
    //     tmp=nums[i]
    //     for j:=i+1;j<len(nums);j++{
    //         if nums[j]==tmp  {
    //             return true
    //         } 
    //     }
    // }
    // return false

    // v3 copied, hash table, fast, 104ms
    appearance := make(map[int]bool)

	for _, num := range nums {
		if _, ok := appearance[num]; ok {
			return true
		}
		appearance[num] = true
	}
	return false
    
}