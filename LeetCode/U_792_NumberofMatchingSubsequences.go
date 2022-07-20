// https://leetcode.com/problems/number-of-matching-subsequences/
// 2022年07月20日 13:00:55

import "fmt"
// v1 two pointer, slow
func isSubsequence(s string, w string) int {
    p1,p2:=0,0
    for p1<len(s) {
        if p2==len(w) {return 1}
        if s[p1]==w[p2] {
            p1++
            p2++
        }else{
            p1++
        }
    }
    if p2==len(w) {return 1}
    return 0
}
func numMatchingSubseq(s string, words []string) int {
    ret:=0
    for i:=0;i<len(words);i++{
        ret+=isSubsequence(s,words[i])
    }
    return ret
}
