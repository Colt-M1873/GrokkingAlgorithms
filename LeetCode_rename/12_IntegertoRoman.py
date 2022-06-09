# https://leetcode.com/problems/integer-to-roman/
# 2022年05月20日 10:52:32

class Solution:
    def intToRoman(self, num: int) -> str:
        # v1 
        arr=[(1000, 'M'), (500, 'D'), (100, 'C'), (50, 'L'), (10, 'X'), (5, 'V'), (1, 'I')]
        ret=''
        for i in range(len(arr)):
            if i%2==1 : # 找出5开头的
                if num//arr[i][0]==1: # 大于5开头的数，如500
                    if num//arr[i+1][0]==9: # 处理9的情况
                        ret=ret+arr[i+1][1]+arr[i-1][1]
                        num=num%(9*arr[i+1][0])
                    else: # 处理 6 7 8
                        ret+=arr[i][1]*(num//arr[i][0])
                        num%=arr[i][0]        
                else: # 不足500
                    if num//arr[i+1][0]==4: # 处理4 
                        ret=ret+arr[i+1][1]+arr[i][1]
                        num=num%(4*arr[i+1][0])            
            else:
                ret+=arr[i][1]*(num//arr[i][0])
                num%=arr[i][0]
        return ret
    
        # v2 copied a more clear and simple way
        d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}         
        res = ""
        for i in d:
            res += (num//i) * d[i]
            num %= i
        return res
        
        # v3 copied, wierd
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return M[num//1000] + C[(num%1000)//100] + X[(num%100)//10] + I[num%10]
        