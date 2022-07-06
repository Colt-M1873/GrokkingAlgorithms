// https://leetcode.com/problems/reverse-string/
// 2022年07月05日 12:34:42

func reverseString(s []byte)  {
    for i,j:=0,len(s)-1;i<j;i,j=i+1,j-1 {
        s[i],s[j]=s[j],s[i]
    }
}