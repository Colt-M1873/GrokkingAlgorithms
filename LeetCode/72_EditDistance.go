// https://leetcode.com/problems/edit-distance/submissions/922901180/
// 2023年03月27日 16:45:46

// https://programmercarl.com/0072.%E7%BC%96%E8%BE%91%E8%B7%9D%E7%A6%BB.html#%E6%80%9D%E8%B7%AF
// 简化思路不考虑增加，只考虑删除操作，因为两边谁长就删除谁，和谁短增加谁是一样的
// 初始dp矩阵的长宽分别为单词长度加一
// 首航和首列均初始化成012345的序列，因为长度为n的字符串和长度为0的空字符串比较时候相当于执行了n次的删除操作
// 随后当某坐标对应的两个字符相等时候，不用操作，即dp[i][j]=dp[i-1][j-1]
// 当两个字符不等的时候，有三种可能的操作
// 一是删除水平j方向上的字符，从左向右递推，即dp[i][j]=dp[i][j-1]+1
// 二是删除垂直i方向上的字符，从上向下递推，即dp[i][j]=dp[i-1][j]+1
// 三是改变字符，相当于把两个字符改成同一个值，即从左上向右下递推，dp[i][j]=dp[i-1][j-1]+1
// 我们没有必要逐个去判断三种情况，只要递推地将三个之中的最小值赋给dp即可
// dp[i][j]总是取的三个方向之中的最小值
// 即 dp[i][j] = min([]int{dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + 1})

func minDistance(word1 string, word2 string) int {
	dp := make([][]int, len(word1)+1)
	for i := 0; i < len(word1)+1; i++ {
		dp[i] = make([]int, len(word2)+1)
	}
	for i := 0; i < len(word1)+1; i++ {
		dp[i][0] = i
	}
	for i := 0; i < len(word2)+1; i++ {
		dp[0][i] = i
	}
	// fmt.Println(dp)

	for i := 1; i < len(word1)+1; i++ {
		for j := 1; j < len(word2)+1; j++ {
			if word1[i-1] == word2[j-1] {
				dp[i][j] = dp[i-1][j-1]
			} else {
				dp[i][j] = min([]int{dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + 1})
			}
		}
	}
	// for _,d:=range dp{
	//     fmt.Println(d)
	// }
	return dp[len(word1)][len(word2)]
}

func min(n []int) int {
	ret := 0
	for i, v := range n {
		if i == 0 || v < ret {
			ret = v
		}
	}
	return ret
}