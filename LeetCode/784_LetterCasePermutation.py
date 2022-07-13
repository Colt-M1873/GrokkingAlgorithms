# https://leetcode.com/problems/letter-case-permutation/
# 2022年07月12日 13:33:11

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        # v1 backtracking, slow
        # permutation of every letter, and of upper and lower case
        ret=[]
        def backtracking(s,path,ret):
            if not s:  # Base case
                ret.append(path)
                return 
            # Recursive case
            if '0'<=s[0]<='9': # if s[0] is num
                backtracking(s[1:],path+s[0],ret)
            else:
                if s[0] > 'Z' : # if s[0] is lowercase
                    cases = [s[0], chr(ord(s[0])-32)]
                else:  # if s[0] is uppercase
                    cases = [chr(ord(s[0])+32), s[0]]
                for char in cases: # permutation of upper and lower case
                    backtracking(s[1:],path+char,ret)
        backtracking(s,'',ret)
        return ret