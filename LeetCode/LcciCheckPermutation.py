# https://leetcode.cn/problems/check-permutation-lcci/
# 2022年09月27日 22:28:34


class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        return Counter(s1) == Counter(s2)