# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
# 2022年09月10日 22:02:41

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # v1 copied https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/39608/A-clean-DP-solution-which-generalizes-to-k-transactions
        # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/54113/A-Concise-DP-Solution-in-Java
        # best explanation
        # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/54125/Very-understandable-solution-by-reusing-Problem-III-idea
        # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75928/share-my-dp-solution-by-state-machine-thinking
        if len(prices)<=1: return 0
        maxProf=0
        p=[0]*len(prices)
        f=[]
        for i in range(k+1):
            f.append(p.copy())
        for kk in range(1,k+1):
            tmpMax=f[kk-1][0]-prices[0] # 当前最大利润减去当前价格，tmpMax means the maximum profit of just doing at most i-1 transactions, using at most first j-1 prices, and buying the stock at price[j] - this is used for the next loop.
            for ii in range(1,len(prices)):
                f[kk][ii]=max(f[kk][ii-1],prices[ii]+tmpMax)
                tmpMax=max(tmpMax,f[kk-1][ii]-prices[ii])
                maxProf=max(f[kk][ii],maxProf)
        return maxProf

        
                