# https://leetcode.cn/problems/largest-substring-between-two-equal-characters/
# 2022年09月17日 15:38:04

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # return 0
        d={}
        retMax=-1
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = i
            else:
                retMax=max(retMax, i-d[s[i]]-1)
        return retMax
            
        # one-liner
        return max(s.rindex(c) - s.index(c) - 1 for c in set(s))


        return max(s.rfind(c) - s.find(c) - 1 for c in set(s))

        return max(map(sub, range(len(s)), map({}.setdefault, s, range(1, len(s) + 1)))) 