# https://leetcode.com/problems/longest-palindrome/
# 2022 3.26

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # v1
        d={}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=1
            else:
                d[s[i]]+=1
        ret=0
        odd=0
        for item in d.keys():
            if d[item]%2==0:
                ret+=d[item]
            else:
                odd=1
                ret+=d[item]-1
        return ret+odd

        # # v2 aucomplete by copilot
        # if not s: return 0
        # d={}
        # for c in s:
        #     d[c]=d.get(c,0)+1
        # ans=0
        # for k in d:
        #     if d[k]%2==0:
        #         ans+=d[k]
        #     else:
        #         ans+=d[k]-1
        # if ans<len(s):
        #     ans+=1
        # return ans

        # # v3 using set to reord all odd letters and reduce them from total length 
        # hash = set()
        # for c in s:
        #     if c not in hash:
        #         hash.add(c)
        #     else:
        #         hash.remove(c)
        # # len(hash) is the number of the odd letters
        # return len(s) - len(hash) + 1 if len(hash) > 0 else len(s)

        # # v4 oneliner using collections.Counter? 
        # # from  https://leetcode.com/problems/longest-palindrome/discuss/89587/What-are-the-odds-(Python-and-C%2B%2B)
        # odds = sum(v & 1 for v in collections.Counter(s).values())
        # return len(s) - odds + bool(odds)
        # # v4.1 oneliner 
        # use = sum(v & ~1 for v in collections.Counter(s).values())
        # return use + (use < len(s))
        # # v4.2 oneliner
        # counts = collections.Counter(s).values()
        # return sum(v & ~1 for v in counts) + any(v & 1 for v in counts)


        