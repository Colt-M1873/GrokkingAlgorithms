// https://leetcode.com/problems/maximum-length-of-repeated-subarray/
// 2023年03月27日 15:31:12

// https://programmercarl.com/0718.%E6%9C%80%E9%95%BF%E9%87%8D%E5%A4%8D%E5%AD%90%E6%95%B0%E7%BB%84.html#%E6%80%9D%E8%B7%AF
func findLength(nums1 []int, nums2 []int) int {
	dp := make([][]int, len(nums1)+1)
	for i := 0; i < len(nums1)+1; i++ {
		dp[i] = make([]int, len(nums2)+1)
	}
	// fmt.Println(dp)
	ret := 0
	for i := 1; i < len(nums1)+1; i++ {
		for j := 1; j < len(nums2)+1; j++ {
			if nums1[i-1] == nums2[j-1] {
				dp[i][j] = dp[i-1][j-1] + 1
				ret = int(math.Max(float64(dp[i][j]), float64(ret)))
			}
		}
	}
	// for _, d:=range dp{
	//     fmt.Println(d)
	// }
	return ret
}