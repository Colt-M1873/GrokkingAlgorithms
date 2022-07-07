# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# 2022年04月02日 13:15:43
# 2022年07月07日 11:57:20

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # # v1 ，slow using set(), 731ms
        # if len(s)<2:return len(s)
        # l=0
        # r=0
        # m=0
        # while l<len(s):
        #     while len(set(list(s[l:r])))==len(s[l:r]) and l<len(s):
        #         if r<len(s):
        #             r+=1
        #         else:
        #             m=max(m,len(s[l:r]))
        #             l+=1
        #     m=max(m,len(s[l:r-1]))
        #     while len(set(list(s[l:r])))<len(s[l:r]):
        #         l+=1
        # return m 

        # # v1.1 using hashtable, faster, 79ms
        # seen={}
        # l=0
        # r=0
        # m=0
        # while l<len(s):
        #     while r<len(s) and s[r] not in seen and l<len(s) :
        #         seen[s[r]]=True
        #         r+=1
        #     m=max(m,r-l)
        #     if r==len(s):
        #         r-=1
        #     while s[r] in seen and l<len(s):
        #         seen.pop(s[l],None)
        #         l+=1
        # return m

        # # v1.2 more clear
        # seen={}
        # l=0
        # r=0
        # m=0
        # while l<len(s):
        #     if r<len(s) and s[r] not in seen:
        #         seen[s[r]]=True
        #         r+=1
        #     else:
        #         seen.pop(s[l],None)
        #         l+=1
        #     m=max(m,r-l)
        # return m


        # v2 copied, classic sliding window
        # https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/347818/Python3%3A-sliding-window-O(N)-with-explanation
        seen = {}
        l = 0
        output = 0
        for r in range(len(s)):
            # If s[r] not in seen, we can keep increasing the window size by moving right pointer
            if s[r] not in seen:
                output = max(output,r-l+1)
            # There are two cases if s[r] in seen:
            # case1: s[r] is inside the current window, we need to change the window by moving left pointer to seen[s[r]] + 1.
            # case2: s[r] is not inside the current window, we can keep increase the window
            else:
                if seen[s[r]] < l:
                    output = max(output,r-l+1)
                else:
                    l = seen[s[r]] + 1
            seen[s[r]] = r
        return output

        # v3 copied 
        # https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1781/Python-solution-with-comments.
        # dic, res, start, = {}, 0, 0
        # for i, ch in enumerate(s):
        #     # when char already in dictionary
        #     if ch in dic:
        #         # check length from start of string to index
        #         res = max(res, i-start)
        #         # update start of string index to the next index
        #         start = max(start, dic[ch]+1)
        #     # add/update char to/of dictionary 
        #     dic[ch] = i
        # # answer is either in the begining/middle OR some mid to the end of string
        # return max(res, len(s)-start)


        # 2022年07月07日 11:57:15
        # # va1 sliding window using list
        # l,r=0,0
        # d=[]
        # maxlen=0
        # # d.pop(3)# must pop or delete a valid key or will trhow error
        # while r<len(s):
        #     if s[r] not in d:
        #         d.append(s[r])
        #         r+=1
        #     else:
        #         # maxlen=max(maxlen,r-l-1)
        #         maxlen=max(maxlen,len(d))
        #         ind=d.index(s[r])
        #         # print(d,ind,s[r])
        #         l+=ind+1
        #         d=d[ind+1:]
        #         d.append(s[r])
        #         r+=1
        #         # print(d)
        # maxlen=max(maxlen,len(d))
        # return maxlen
        
        # va1.1 sliding window using list, simplified
        r=0
        d=[]
        maxlen=0
        while r<len(s):
            if s[r] in d:
                maxlen=max(maxlen,len(d))
                ind=d.index(s[r])
                d=d[ind+1:]
            d.append(s[r])
            r+=1
        maxlen=max(maxlen,len(d))
        return maxlen
        
        