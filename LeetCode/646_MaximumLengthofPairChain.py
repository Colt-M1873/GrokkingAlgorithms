# https://leetcode.cn/problems/maximum-length-of-pair-chain/
# 2022年09月03日 10:08:59


# v1 slow, dp 2256ms
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[0])
        dp=[1]*len(pairs)
        for i in range(len(pairs)):
            for j in range(i):
                if pairs[i][0]>pairs[j][1]:
                    dp[i]=max(dp[i],dp[j]+1)
        return dp[-1]


# v2 greedy, fast
# excellent proof of greedy method https://leetcode.com/problems/maximum-length-of-pair-chain/discuss/225801/Proof-of-the-greedy-solution
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[1])
        ret=0
        curr=-inf # current tail of the whole chain
        for head,tail in pairs:
            if curr<head:
                ret+=1
                curr=tail
        return ret

# v2.1 greedy
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        cur, res = float('-inf'), 0
        for p in sorted(pairs, key=lambda x: x[1]):
            if cur < p[0]: cur, res = p[1], res + 1
        return res