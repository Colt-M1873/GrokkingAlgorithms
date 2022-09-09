# https://leetcode.cn/problems/rearrange-spaces-between-words/submissions/
# 2022年09月07日 18:59:40

class Solution:
    def reorderSpaces(self, text: str) -> str:
        l=list(text.split())
        tlen=len(text)
        slen=len(''.join(l))
        if tlen==slen: return text
        if len(l)==1:
            return l[0]+' '*(tlen-slen)
        distance = (tlen-slen)//(len(l)-1)
        remain = (tlen-slen)%(len(l)-1)
        return (' '*distance).join(l)+(' '*remain)
