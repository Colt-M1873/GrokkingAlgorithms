# https://leetcode.com/problems/maximum-swap/
# 2022 3.24

class Solution:
    def maximumSwap(self, num: int) -> int:

        # # v1 like bubble sort.
        # l=list(str(num))
        # currmax=num
        # for i in range(len(l)):
        #     for j in range(i+1,len(l)):
        #         if l[i]<l[j]:
        #             l[i], l[j]=l[j], l[i]
        #             if int(''.join(l))>currmax:
        #                 currmax=int(''.join(l))
        #                 print(currmax)
        #                 print(i,j)
        #                 maxi=i                
        #             l[i],l[j]=l[j],l[i]
        # return currmax

        # # v1.1 
        # l=list(str(num))
        # currmax=num
        # maxi=len(l)
        # for i in range(len(l)):
        #     if i>maxi: # 如果i比当前最大的i还靠后的话，交换之后的值必然比当前最大值小。例如1234当千位交换到最大4231后，百位再怎么交换（最大也就是1432）也不会超过千位交换获得的最大值。
        #         break
        #     for j in range(i+1,len(l)):
        #         if l[i]<l[j]:
        #             l[i], l[j]=l[j], l[i]
        #             if int(''.join(l))>currmax:
        #                 currmax=int(''.join(l))
        #                 print(currmax)
        #                 print(i,j)
        #                 maxi=i                
        #             l[i],l[j]=l[j],l[i]
        # return currmax

        # v1.2 just return after searching the first j loop
        l=list(str(num))
        currmax=num
        maxi=len(l)
        i=0
        while i<maxi:
            for j in range(i+1,len(l)):
                if l[i]<l[j]:
                    l[i], l[j]=l[j], l[i]
                    if int(''.join(l))>currmax:
                        currmax=int(''.join(l))
                        print(currmax)
                        print(i,j)
                        maxi=i                
                    l[i],l[j]=l[j],l[i]
            i+=1
        return currmax


        # 2022年09月13日 22:21:19
        # v2 greedy
        orignum=num
        n=[]
        while num>0:
            n.insert(0,num%10)
            num//=10
        sn=sorted(n,reverse=True)
        left,right=-1,-1
        for i in range(len(n)):
            if n[i]!=sn[i]:
                left=i
                break
        if left==-1:
            return orignum
        for j in range(len(n)-1,-1,-1):
            if n[j]==sn[left]:
                right=j
                break
        n[left],n[right]=n[right],n[left]
        ret=0
        for item in n:
            ret=10*ret+item
        return ret