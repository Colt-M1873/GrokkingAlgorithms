# https://leetcode.com/problems/string-to-integer-atoi
# 2022年04月02日 13:14:04

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # print(int("2.1")) #会报错，带小数的字符串不能直接转int，需要先转float再转int
        # print(int(float("2.1"))) # 正确  
        if not s: return 0
        ret=[]
        for item in list(s):
            if '0'<=item<='9' or (item in ['+','-'] and  not ret)  or (item == '.' and '.' not in ret):
                ret.append(item)
            else:
                if ret:
                    break
                if item != " " and not ret:
                    return 0
        if not ret or ret==['-'] or ret== ['+']:
            return 0
        ret=int(float(''.join(ret)))
        return max(min(ret,2**31-1),-2**31)
