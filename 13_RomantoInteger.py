
# https://leetcode.com/problems/roman-to-integer/


class Solution:
    def romanToInt(self, s: str) -> int:
            Dic1={
                '0':0,
                'I':1,
                'V':5,
                'X':10,
                'L':50,
                'C':100,
                'D':500,
                'M':1000
            }
            sum=0
            # s='MCMXCIV'
            s=s+'0'
            for i in range(len(s)-1):
                thisnum=Dic1[s[i]]
                if Dic1[s[i]]<Dic1[s[i+1]]:
                    thisnum=-Dic1[s[i]]
                sum+=thisnum
            return sum