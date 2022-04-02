# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# 2022年04月02日 13:15:43

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # v1 ，slow
        if len(s)<2:return len(s)
        l=0
        r=0
        m=0
        while l<len(s):
            while len(set(list(s[l:r])))==len(s[l:r]) and l<len(s):
                if r<len(s):
                    r+=1
                else:
                    m=max(m,len(s[l:r]))
                    l+=1
            m=max(m,len(s[l:r-1]))
            while len(set(list(s[l:r])))<len(s[l:r]):
                l+=1
        return m 