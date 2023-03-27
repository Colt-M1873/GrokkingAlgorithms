// https://leetcode.cn/problems/n-th-tribonacci-number/
// 2023年03月25日 15:41:20
func tribonacci(n int) int {
	a0 := 0
	a1 := 1
	a2 := 1
	a3 := 0
	if n == 0 {
		return 0
	}
	if n <= 2 {
		return 1
	}
	for i := 2; i < n; i++ {
		a3 = a0 + a1 + a2
		a0 = a1
		a1 = a2
		a2 = a3
	}
	return a3
}

// recurtsive TLE
// 2023年03月25日 15:42:24
func tribonacci(n int) int {
	if n <= 0 {
		return 0
	}
	if n <= 2 {
		return 1
	}
	return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)
}