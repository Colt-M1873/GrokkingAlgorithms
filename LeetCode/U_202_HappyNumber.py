# https://leetcode.com/problems/happy-number/
# 2022年04月22日 14:59:28

class Solution:
    def isHappy(self, n: int) -> bool:
        q=[]
        ans=0
        while ans!=1:
            ans=0
            while n!=0:
                ans+=(n%10)**2
                n=(n-n%10)//10
            n=ans
            if ans not in q:
                q.append(ans)
            else:
                return False
            # print(ans)
        return True