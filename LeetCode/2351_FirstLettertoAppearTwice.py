# https://leetcode.com/problems/first-letter-to-appear-twice/
# 2022年07月25日 14:12:05
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d={}
        for i in range(len(s)):
            if s[i] in d:
                return s[i]
            else:
                d[s[i]]=0
        