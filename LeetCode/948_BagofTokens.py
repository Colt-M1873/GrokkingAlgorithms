# https://leetcode.com/problems/bag-of-tokens/
# 2022年09月12日 22:06:27

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # 原则是用power来翻代价最小的token
        # 用score来翻收益最大的token
        # v1 greedy + two pointer
        s=0
        smax=0
        tokens.sort()
        l,r=0,len(tokens)-1
        # print(tokens)
        if len(tokens)==1:return int(power>=tokens[0])
        while l<r:
            if tokens[l]>power and s==0:
                return smax
            while tokens[l]<=power and l<=r:
                power-=tokens[l]
                # print("consume power")
                # print(tokens[l])
                s+=1
                smax=max(s,smax)
                l+=1
            if s>0 and l<=r:
                s-=1
                # print("consume score")
                # print(tokens[r])
                power+=tokens[r]
                r-=1
        return smax
                
            
            
        
            