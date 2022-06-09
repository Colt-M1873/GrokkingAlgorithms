# https://leetcode.com/problems/isomorphic-strings/
# 2022年04月23日 21:58:26

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # 重要的是发现规律，
        # 先用set提取出所含的字母，去掉重复，然后用set中的每一个字母去另一个字符串里替换，如果替完相同就是valid的
        
        #不能直接用set否则顺序会乱
        # sset=list(set(list(s)))
        # tset=list(set(list(t)))
        sset=[]
        tset=[]
        for i in range(len(s)):
            
            if s[i] not in sset:
                sset.append(s[i])
            
            if t[i] not in tset:
                tset.append(t[i])
            if len(sset)!=len(tset):
                return False
            if sset.index(s[i])!=tset.index(t[i]):
                return False
            
        return True
        # print(sset)
        # print(tset)
        # if len(sset)!=len(tset):
        #     return False
        # j=0
        # for i in range(len(t)):
        #     if t==s:
        #         return True
        #     print(j)
        #     if t[i] not in sset[:j]:
        #         print(i)
        #         print(t[i])
        #         print(sset[j])
        #         t=t.replace(t[i],sset[j])
        #         print(t)
        #         j+=1
        # # for i in range(len(s)):
        # #     s=s.replace(s[i],t[i])
        # #     print(s)
        # #     if s==t:
        # #         return True
        # # return False