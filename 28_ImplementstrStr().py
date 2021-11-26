# https://leetcode.com/problems/implement-strstr/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # v1 oneliner using builtin str.find(), clean and fast  64ms
        return haystack.find(needle)
    
        # # v2  copied, without builtin functions, but really slow 112ms
        # for i in range(0, len(haystack) - len(needle) + 1):
        #     if haystack[i:i+len(needle)] == needle:
        #         return i
    
        # return -1
    
    
        # # v3 copied KMP tree, brilliant string match algorithm, but just as fast as builtin str.find, 69ms
        # # copied from https://leetcode.com/problems/implement-strstr/discuss/665448/AC-simply-readable-Python-KMP-Rabin-Karp
        # n, h = len(needle), len(haystack)
        # i, j, nxt = 1, 0, [-1]+[0]*n
        # while i < n:                                # calculate next array
        #     if j == -1 or needle[i] == needle[j]:   
        #         i += 1
        #         j += 1
        #         nxt[i] = j
        #     else:
        #         j = nxt[j]
        # i = j = 0
        # while i < h and j < n:
        #     if j == -1 or haystack[i] == needle[j]:
        #         i += 1
        #         j += 1
        #     else:
        #         j = nxt[j]
        # return i-j if j == n else -1


        # # v4 copied  Rabin Karp  200ms+
        # n, h = len(needle), len(haystack)
        # hash_n = hash(needle)
        # for i in range(h-n+1):
        #     if hash(haystack[i:i+n]) == hash_n:
        #         return i
        # return -1