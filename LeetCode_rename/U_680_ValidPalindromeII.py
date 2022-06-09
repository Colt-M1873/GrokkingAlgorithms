# https://leetcode.com/problems/valid-palindrome-ii/
# 2022 4.03

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s==s[::-1]: return True
        l=0
        r=len(s)-1
        # if r==1:return True
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            elif s[l+1:r+1]==s[l+1:r+1][::-1]:
                return True
            elif s[l:r]==s[l:r][::-1]:
                return True
            else:
                return False
        return False