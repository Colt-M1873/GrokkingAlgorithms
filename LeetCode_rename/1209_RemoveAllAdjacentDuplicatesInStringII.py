# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
# 2022年05月06日 19:12:29

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # # v1 modified stack, too slow 6300ms
        # stack=[]
        # for i in range(len(s)):
        #     # record both the character and the samecount
        #     if not stack or s[i]!=stack[-1][0]:
        #         stack.append((s[i],1))
        #     else:
        #         stack.append((s[i],stack[-1][1]+1))
        #         if stack[-1][1]==k: # when last k character are the same then delete them
        #             stack=stack[:-k]
        # return ''.join(map(lambda x:x[0],stack))
        
        # # v1.1 using pop instead of reassigning the whole stack, way faster, 182ms, 38.43%
        # stack=[]
        # for i in range(len(s)):
        #     # record both the character and the samecount
        #     if not stack or s[i]!=stack[-1][0]:
        #         stack.append((s[i],1))
        #     else:
        #         stack.append((s[i],stack[-1][1]+1))
        #         if stack[-1][1]==k: # when last k character are the same then delete them
        #             # for _ in range(k): # faster 
        #             #     stack.pop()
        #             del stack[-k:] # fastest
        # return ''.join(map(lambda x:x[0],stack))
        
        # # V2 copied two pointer 180ms
        # #https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/discuss/392933/JavaC%2B%2BPython-Two-Pointers-and-Stack-Solution
        # slow=fast=0
        # count=[0]*len(s)
        # s=list(s)
        # while fast<len(s):
        #     s[slow]=s[fast]
        #     if s[slow]==s[slow-1]:
        #         count[slow]=count[slow-1]+1
        #     else:
        #         count[slow]=1
        #     if count[slow]==k:
        #         slow-=k
        #     slow+=1
        #     fast+=1
        # return ''.join(s[:slow])
        
        # v3 another kind of stack, more easy to undersand and faster, 103ms
        stack = [['#', 0]]
        for c in s:
            if stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        return ''.join(c * k for c, k in stack)
        
        