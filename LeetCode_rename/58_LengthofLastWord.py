# https://leetcode.com/problems/length-of-last-word/
# 2021 11.30

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # # v1 oneliner boring builtin functions
        # return len(s.split()[-1])

        # v2 no builtin function
        for i in range(len(s)-1,-1,-1):
            if s[i]!=' ':
                for j in range(i,-1,-1):
                    if s[j]==' ':
                        return i-j
                return i+1
        return 0

