class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        outstr=''
        j=0
        while 1:
            for i in range(len(strs)-1):
                try:
                    if strs[0][j]==strs[i][j]:
                        continue
                    else:
                        break 
                except:
                    break
            j+=1
        return outstr+strs[0][:j]