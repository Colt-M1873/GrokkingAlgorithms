// https://leetcode.cn/problems/final-prices-with-a-special-discount-in-a-shop/
// 2022年09月01日 14:21:56

// v1 simple simulation
import "fmt"
func finalPrices(prices []int) []int {
    for  i:=range prices {
        for j:=i+1;j<len(prices);j++{
            if prices[j]<=prices[i]{
                prices[i]-=prices[j]
                break
            }
        }
    }
    return prices
}
// v2 monotonic stack
func finalPrices(prices []int) []int {
    l:=len(prices)
    ms:=[]int{0}
    ret:=make([]int,l)
    for i:=l-1;i>=0;i--{
        p:=prices[i]
        for len(ms)>1 && ms[len(ms)-1]>p{
            ms=ms[:len(ms)-1]
        }
        ret[i]=p-ms[len(ms)-1]
        ms=append(ms,p)
    }
    return ret
}


// v3 monitonic srack storing index
func finalPrices(prices []int) []int {
    ms:=[]int{}
    for i:=range prices{
        p:=prices[i]
        for len(ms)>0 && prices[ms[len(ms)-1]]>=p{
            prices[ms[len(ms)-1]]-=p
            ms=ms[:len(ms)-1]
        }
        ms=append(ms,i)
    }
    return prices
}