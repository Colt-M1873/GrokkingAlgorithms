# https://leetcode.cn/problems/final-prices-with-a-special-discount-in-a-shop/
# 2022年09月01日 15:37:39

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # v1 双循环，模拟
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j]<=prices[i]:
                    prices[i]-=prices[j]
                    break
        return prices
        
        
        # 官方题解方案，倒序遍历prices，保证栈的单调性，
        # 题目描述是正向的，正序遍历，对于每个元素prices[i]找下一个不大于它本身的元素
        # 以上描述等价于：
        # 倒序遍历，对于原数组的每个元素price[i]，找到上一个小于等于他的元素，
        # 而单调栈正是起到这样一个从小到大记录的作用，ms[-1]恰好就是上一个小于等于当前值的元素
        l=len(prices)
        ms=[0] # monotonic stack
        ret=[0]*l # to be returned
        for i in range(l-1,-1,-1):
            p=prices[i]
            while ms and ms[-1]>p:
                ms.pop()
            ret[i]=p-ms[-1]
            ms.append(p)
        return ret

        ## v2 用栈代替双循环，栈中存储递增序列的index
        ms=[] # monotonic stack, 存储上一个最大值的index
        for idx, p in enumerate(prices):
            while ms and prices[ms[-1]]>=p:
                prices[ms.pop()]-=p
            ms.append(idx)
        return prices
        # 这种方法的复杂度该怎样分析呢？时间和空间复杂度貌似都是O(n)
        # 但在输入数组纯递增的情况下这种方法是比双循环要快的

        
