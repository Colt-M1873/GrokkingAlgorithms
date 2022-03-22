#  https://leetcode.com/problems/validate-stack-sequences
# 2022 3.16

class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        # # v1 cmoplicated, two pointer pointing two array
        # stack=[]
        # i,j=0,0
        # while j<len(popped):
        #     if i<len(pushed):
        #         if not stack or stack[-1]!=popped[j]:
        #             stack.append(pushed[i])
        #             i+=1
        #         elif stack[-1]==popped[j]:
        #             stack.pop()
        #             j+=1;
        #     else:
        #         if stack[-1]!=popped[j]:
        #             return False
        #         else:
        #             stack.pop()
        #             j+=1;
        # return True        
    
        # v1.1 cmoplicated, two pointer pointing two array
        stack=[]
        i,j=0,0
        while j<len(popped):
            if i<len(pushed):
                if not stack or stack[-1]!=popped[j]:
                    stack.append(pushed[i])
                    i+=1
            else:
                if stack[-1]!=popped[j]:
                    return False
            if stack and stack[-1]==popped[j]:
                stack.pop()
                j+=1
        return True