# https://leetcode.com/problems/permutation-in-string/
# 2022年07月06日 15:15:12

from itertools import permutations
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # # v1 failed, TLE
        # listing all permutations are wasting sapce and time
        # if len(s2)<len(s1): return False
        # perms = [''.join(p) for p in permutations(s1)]
        # perm_d=dict.fromkeys(perms,None)
        # letter_d=dict.fromkeys(list(s1),None)
        # # print(letter_d)
        # for i in range(len(s2)):
        #     if s2[i] in letter_d:
        #         if i<=len(s2)-len(s1) and s2[i:i+len(s1)] in perm_d:
        #             return True
        # return False
        
        # # v2 not sliding window, too slow， 9051ms
        # d_s1=dict.fromkeys(set(s1),0)
        # for i in range(len(s1)):
        #     d_s1[s1[i]]+=1
        # # print(d_s1)
        # l1,l2=len(s1),len(s2)
        # for i in range(l2):
        #     if i<=l2-l1 and s2[i] in d_s1:
        #         d_s2=dict.fromkeys(set(s2[i:i+l1]),0)
        #         for j in range(l1):
        #             d_s2[s2[i+j]]+=1
        #         # print(d_s2)
        #         if d_s1==d_s2:
        #             return True

        # v3 alphabet dict and sliding window, superfast, 57ms
        # permutation means the same frequency of letter
        d={}
        for i in range(ord('a'),ord('z')+1):
            d[chr(i)]=0
        d_s1=d.copy()
        d_s2=d.copy()
        for i in range(len(s1)):
            d_s1[s1[i]]+=1
        l1=len(s1)
        l2=len(s2)
        for j in range(len(s2)):
            if j<l1:
                d_s2[s2[j]]+=1
            else:
                d_s2[s2[j]]+=1
                d_s2[s2[j-l1]]-=1
            if d_s1==d_s2:
                return True

        # # v3.1 
        # # sliding window with dict
        # abd={} #alphabet dict
        # alphabet=[chr(x) for x in range(ord('a'),ord('z')+1)]
        # abd=dict.fromkeys(alphabet,0)
        # s1d,s2d=abd.copy(),abd.copy()
        # for i in range(len(s1)):
        #     s1d[s1[i]]+=1
        # l1=len(s1)
        # for i in range(len(s2)):
        #     if i>=l1:
        #         s2d[s2[i-l1]]-=1
        #     s2d[s2[i]]+=1
        #     if s2d==s1d:
        #         return True
        # return False
    
        # # v4 copied, collections.Counter(), slow, 1378ms
        # ctr1 = collections.Counter(s1)
        # i = 0
        # while i < len(s2) - len(s1) + 1:
        #     if s2[i] in ctr1:
        #         ctr2 = collections.Counter(s2[i: i+len(s1)])
        #         if ctr1 == ctr2: return True
        #     i += 1
        # return False