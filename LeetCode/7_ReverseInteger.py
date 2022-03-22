# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        
        # # v1 str compare
        # outputstr=''
        # listx=list(str(abs(x)))
        # if len(listx)>1 and listx[-1]=='0':
        #     listx.pop(-1)
        # if x<0:
        #     outputstr+='-'
        # for i in range(len(listx)):
        #     outputstr=outputstr+listx[-i-1]
        # outint=int(outputstr)
        # if outint>2**31-1 or outint<-2**31:
        #     return 0
        # return outint
             
        # # v2
        # sum=0
        # savex=x # save original x to set output sign
        # x=abs(x)
        # while x!=0:
        #     sum=sum*10+x%10
        #     x=int(x/10)
        # if sum<-2**31 or sum > 2**31-1:
        #     return 0
        # if savex<0: # set output sign
        #     return -sum
        # return sum

        # v2.1  use x//abs(x) to solve negative problem
        sum=0
        while x!=0:
            sum=sum*10+x%(10*x//abs(x))
            x=int(x/10)
        if sum<-2**31 or sum > 2**31-1:
            return 0
        return sum