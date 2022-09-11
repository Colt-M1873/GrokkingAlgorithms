# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# 2021 12.18 2022 3.10

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # # cant use recursive because a long input will exceed time or memory limit
        # # v1 iterative, slow, 7916ms
        # ret=0
        # newlist=[prices[0]]
        # # first get rid of all continuous same item in input list,
        # while prices:
        #     if prices[0]!=newlist[-1]:
        #         newlist.append(prices.pop(0))
        #     else:
        #         prices.pop(0)
        # prices=newlist
        #  # then iterativly find all maxprofit in all sublist
        # while prices:    
        #     maxprice=max(prices)
        #     maxindex=prices.index(maxprice)
        #     minprice=min(prices[:maxindex+1])
        #     minindex=prices.index(minprice)
        #     maxprofit=prices[maxindex]-prices[minindex]
        #     if maxprofit>ret:
        #         ret=maxprofit
        #     prices=prices[maxindex+1:]
        # return ret
        
        # # v1.1 modified, faster, 3152ms, skipped all descending and continuous same part 
        # ret=0
        # while prices:
        #     while len(prices)>1 and prices[0]>=prices[1]:
        #         prices.pop(0) 
        #     maxprice=max(prices[:])
        #     maxindex=prices.index(maxprice)
        #     minprice=min(prices[:maxindex+1])
        #     minindex=prices.index(minprice)
        #     maxprofit=prices[maxindex]-prices[minindex]
        #     if maxprofit>ret:
        #         ret=maxprofit
        #     prices=prices[maxindex+1:]
        # return ret

        # # v1.2 modified, faster, 1360ms, 
        # # using pointer instead of reassign the whole array
        # # reduced time and memory cost
        # ret=0
        # left=0
        # length=len(prices)
        # while left<length:
        #     while left<length-1 and prices[left]>=prices[left+1]:
        #         left+=1
        #     maxprice=max(prices[left:])
        #     maxindex=prices[left:].index(maxprice)+left
        #     minprice=min(prices[left:maxindex+1])
        #     minindex=prices[left:maxindex+1].index(minprice)+left
        #     left=minindex
        #     maxprofit=maxprice-minprice
        #     if maxprofit>ret:
        #         ret=maxprofit
        #     left=maxindex+1
        # return ret

        # # v2 just one go, faster, 1080ms
        # # skip all descending part and use variable to record current smallest 
        # # then skip all ascending and use every local max to detract current smallest
        # # record this profit and compare with current max profit
        # currmin=prices[0]
        # currmaxprofit=0
        # currIdx=0
        # while currIdx<len(prices)-1:
        #     while currIdx<len(prices)-1 and prices[currIdx]>=prices[currIdx+1]:
        #         currIdx+=1
        #     if prices[currIdx]<currmin:
        #         currmin=prices[currIdx]
        #     while currIdx<len(prices)-1 and prices[currIdx]<prices[currIdx+1]:
        #         currIdx+=1
        #     if prices[currIdx]-currmin>currmaxprofit:
        #         currmaxprofit=prices[currIdx]-currmin
        # return currmaxprofit

        # # v2.1 copied clean and elegant, 1124ms
        # buy, ans = float('inf'), 0
        # for p in prices:
        #     buy, ans = min(buy, p), max(ans, p-buy)
        # return ans


        # 03.10 dp with minimum array, 1518ms, slow
        dp=[0]*len(prices)
        currmin=prices.copy()
        for i in range(1, len(prices)):
            currmin[i]=min(currmin[i],currmin[i-1])
            dp[i]=max(dp[i-1],prices[i]-currmin[i])
        return max(dp) 
        # 2022年09月10日 19:32:51： should be dp[-1]
        return dp[-1] 
        

        # 2022年09月10日 19:31:28
        dp=[0]*len(prices)
        currmin=prices[0]
        for idx,p in enumerate(prices):
            if p<currmin:
                currmin=p
            else:
                dp[idx]=p-currmin
        return max(dp)


        # 2022年09月10日 19:34:47
        currmax=0
        currmin=prices[0]
        for idx,p in enumerate(prices):
            if p<currmin:
                currmin=p
            else:
                currmax=max(currmax,p-currmin)
        return currmax
        