# https://leetcode.cn/problems/mean-of-array-after-removing-some-elements/
# 2022年09月14日 21:11:33

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        return sum(sorted(arr)[len(arr)//20:-len(arr)//20])/(len(arr)*0.9)
