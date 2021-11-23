# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        
        # # v1 dumb approach  recursivly strip every pair of parentheses
        # leftright = ['(', '{', '[', ')', '}', ']']
        # lrcount = [0, 0, 0, 0, 0, 0]
        # while len(s)>0:
        #     idx0=leftright.index(s[0])
        #     slen=len(s)
        #     for i in range(slen):
        #         # print(i)
        #         # print(s)
        #         idx = leftright.index(s[i])
        #         lrcount[idx] += 1
        #         if lrcount[3]>lrcount[0] or lrcount[4]>lrcount[1] or lrcount[5]>lrcount[2]:
        #             return False
                
        #         if lrcount[idx0]==lrcount[idx0+3]:
        #             if lrcount[0:3]!=lrcount[3:6]:
        #                 return False
        #             if i<len(s)-1:
        #                 substr = s[i+1:len(s)]
        #                 return self.isValid(substr)
        #             else:
        #                 return True
        #     return False

        # # v2 copied  brilliant but slow, using builtin replace
        # while '[]' in s or '()' in s or '{}' in s:
        #     s = s.replace('[]','').replace('()','').replace('{}','')
        # return not len(s)
   
        # # v2.1 copied same as v2
        # while len(s) > 0:
        #     l = len(s)
        #     s = s.replace('()','').replace('{}','').replace('[]','')
        #     if l==len(s): return False
        # return True

        
        # v3 copied  elegant solution using stack          
        d = {'(':')', '{':'}','[':']'} 
        stack = []
        for i in s:
            if i in d:  # 1
                stack.append(i)
            elif len(stack) == 0 or d[stack.pop()] != i:  # 2
                return False
        return len(stack) == 0 # 3
        # 1. if it's the left bracket then we append it to the stack
        # 2. else if it's the right bracket and the stack is empty(meaning no matching left bracket), or the left bracket doesn't match
        # 3. finally check if the stack still contains unmatched left bracket

