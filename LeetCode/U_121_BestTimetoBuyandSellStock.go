// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/
// 2022年07月20日 12:08:25

func maxProfit(prices []int) int {
    currMin:=prices[0]
    // dp:=[]int{} // storing every element minus current minimum, i.e. maxProfit in this element
    maxPro:=0 // maxProfot till now
    for i:=0;i<len(prices);i++{
        if prices[i]<currMin{
            currMin=prices[i]
        }
        if prices[i]-currMin>maxPro{
            maxPro=prices[i]-currMin
        }
    }
    return maxPro
}