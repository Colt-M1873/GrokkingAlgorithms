# https://leetcode.com/problems/longest-common-prefix/submissions/
# 2021 11.21

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # # v1
        # outstr=''
        # j=0
        # if len(strs)==1:
        #     return strs[0]
        # while 1:
        #     for i in range(len(strs)):
        #         if len(strs[i])==0:
        #             return outstr
        #         if j<len(strs[i]):
        #             if strs[0][j]!=strs[i][j]:
        #                 return outstr+strs[0][:j]                    
        #         else:
        #             return outstr+strs[0][:j]
        #     j+=1
        # return outstr+strs[0][:j]
        
        
        # strs=["aaaaaaaaa","aaaaaaaaaa","a"]
        
        
        # v2 copied  elegant solution using *strings and zip()
        if not strs:
            return ""
        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)
        
        
        # # v3 copied  builtin min with length as key to get shortest str
        # if not strs:
        #     return ""
        # shortest = min(strs,key=len)
        # for i, ch in enumerate(shortest):
        #     for other in strs:
        #         if other[i] != ch:
        #             return shortest[:i]
        # return shortest 
