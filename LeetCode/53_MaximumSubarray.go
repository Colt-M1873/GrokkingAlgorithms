// https://leetcode.com/problems/maximum-subarray/
// 2023年03月25日 16:19:00
// still no idea
func maxSubArray(nums []int) int {
	maxVal := nums[0]
	for i := 1; i < len(nums); i++ {
		if nums[i-1]+nums[i] > nums[i] {
			nums[i] += nums[i-1]
		}
		if nums[i] > maxVal {
			maxVal = nums[i]
		}
	}
	return maxVal
}