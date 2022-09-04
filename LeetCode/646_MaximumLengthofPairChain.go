// https://leetcode.cn/problems/maximum-length-of-pair-chain/
// 2022年09月03日 11:11:02




// v2 greedy, fast
// excellent proof of greedy method https://leetcode.com/problems/maximum-length-of-pair-chain/discuss/225801/Proof-of-the-greedy-solution
import ("fmt" 
        "math")
func findLongestChain(pairs [][]int) int {
    sort.Slice(pairs, func(i,j int) bool {return pairs[i][1]<pairs[j][1]}) // 以[1]为key升序
    ret, curr:= 0, math.MinInt
    for _,p := range pairs {
        if curr<p[0]{
            curr=p[1]
            ret++
        }
    }
    return ret
}