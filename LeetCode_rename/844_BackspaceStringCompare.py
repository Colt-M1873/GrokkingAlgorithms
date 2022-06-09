# https://leetcode.com/problems/backspace-string-compare/
# 2022年05月01日 21:42:03

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # v1 
        def convert(s):
            s1=''
            for i in range(len(s)):
                if s[i]=="#":
                    if len(s1)>0:
                        s1=s1[:-1]
                else:
                    s1+=s[i]
            return s1
        return convert(s)==convert(t)