// https://leetcode.com/problems/reverse-words-in-a-string-iii/submissions/
// 2022年07月05日 16:39:29

import (
    "fmt"
    "strings"
)
func reverseWords(s string) string {
    list_s := strings.Split(s, " ")
    for i:=0;i<len(list_s);i++{
        list_s[i]=reverse(list_s[i])
    }
    return strings.Join(list_s," ")
}

func reverse(s string) string{
    ls := strings.Split(s, "")
    for i,j:=0,len(s)-1 ; i<j ; i,j=i+1,j-1{
        ls[i],ls[j]=ls[j],ls[i]
    }
    return strings.Join(ls,"")
}