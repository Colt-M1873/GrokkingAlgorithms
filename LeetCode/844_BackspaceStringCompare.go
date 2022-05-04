// https://leetcode.com/problems/backspace-string-compare/submissions/
// 2022年05月02日 12:50:10

func backspaceCompare(s string, t string) bool {
    // v1 
    nestedconvert:=func (s string) string {
        s1:=""
        for i:=0;i<len(s);i++{
            if s[i]=='#'{
                if len(s1)>0{
                    s1=s1[:len(s1)-1]
                }
            }else{
                s1+=string(s[i])
            }
        }
        return s1
    }
    return nestedconvert(s)==nestedconvert(t)
}
