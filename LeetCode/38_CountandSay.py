# https://leetcode.com/problems/count-and-say/
# 2022年10月18日 19:01:36

class Solution:
    def countAndSay(self, n: int) -> str:
        retStr='1'
        while n>1:
            retStr=self.num2count(retStr)
            n-=1
        return retStr
    
    def num2count(self,s: str) -> str:
        ret=''
        curr=s[0]
        count=1
        for i in range(1,len(s)):
            if s[i]==curr:
                count+=1
            else:
                ret+=str(count)+curr
                curr=s[i]
                count=1
        ret+=str(count)+curr
        return ret