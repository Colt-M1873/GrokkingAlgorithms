# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # v1 oneliner 28ms 93.36% convert to binary then srt and cut string
        return str(bin(int(a,2)+int(b,2)))[2:]
        
        # # v2  add by bits
        # if len(a)<len(b):
        #     a='0'*(len(b)-len(a))+a
        # else:
        #     b='0'*(len(a)-len(b))+b
        # carry=0
        # out=''
        # for i in range(len(a)-1,-1,-1):
        #     c=int(a[i])+int(b[i])+carry
        #     if c>=2:
        #         out+=str(c%2)
        #         carry=1
        #     else:
        #         out+=str(c)
        #         carry=0
        # if carry==1:
        #     out+='1'
        # return out[::-1]

        # # v2.1 copied  using `or` to judge if a or b or c came to an end
        # carry = 0
        # result = ''
        # a = list(a)
        # b = list(b)
        # while a or b or carry:
        #     if a:
        #         carry += int(a.pop())
        #     if b:
        #         carry += int(b.pop())
        #     result += str(carry %2)
        #     carry //= 2
        # return result[::-1]



# a='1111'
# b='1111'        
# s=Solution()
# print(s.addBinary(a,b))