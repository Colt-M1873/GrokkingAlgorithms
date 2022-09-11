# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# 2022年09月10日 19:49:19

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         # v1 137ms 15.3MB
#         prices.append(-1) # because we detect downfall, so we need to manually create downfall in the end of all prices, or the last section of profit wont be counted
#         currmin=[0]*len(prices)
#         currmin[0]=prices[0]
#         ret=0
#         for i in range(1,len(prices)):
#             if prices[i]<prices[i-1]: # detect downfall and make profit before dowanfall
#                 currmin[i]=prices[i]
#                 ret+=prices[i-1]-currmin[i-1]
#             else:
#                 currmin[i]=currmin[i-1]
#         return ret        
        
        # v1.1 133ms 15.1MB
        prices.append(-1) # because we detect downfall, so we need to manually create downfall in the end of all prices, or the last section of profit wont be counted
        currmin=prices[0]
        ret=0
        for i in range(1,len(prices)):
            if prices[i]<prices[i-1]: # detect downfall and make profit before dowanfall
                ret+=prices[i-1]-currmin
                currmin=prices[i]
        return ret