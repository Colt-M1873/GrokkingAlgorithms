// https://leetcode.com/problems/happy-number/submissions/
// 2022年04月22日 15:52:53

func isHappy(n int) bool {
    var q []int
    ans:=0
    for ;ans!=1; {
        ans=0
        for ;n!=0; {
            ans+=int(math.Pow(float64(n%10),2))
            n=(n-n%10)/10
        }
        n=ans
        // fmt.Println(ans)
        for i:=0;i<len(q);i++ {
            if q[i]==ans {
                // fmt.Println("same found")
                return false
            }
        }
        q=append(q,ans)
    }
    return true
}