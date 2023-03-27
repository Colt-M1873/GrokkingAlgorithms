// https://leetcode.com/problems/fibonacci-number/description/?envType=study-plan&id=dynamic-programming-i
// 2023年03月25日 15:48:19
func fib(n int) int {
	a0 := 0
	a1 := 1
	if n == 0 {
		return 0
	}
	if n == 1 {
		return 1
	}

	var a2 int
	for i := 2; i <= n; i++ {
		a2 = a1 + a0
		a0 = a1
		a1 = a2
	}
	return a2
}

// recursive
// 2023年03月25日 15:49:07
func fib(n int) int {
	if n == 0 {
		return 0
	}
	if n == 1 {
		return 1
	}
	return fib(n-1) + fib(n-2)
}