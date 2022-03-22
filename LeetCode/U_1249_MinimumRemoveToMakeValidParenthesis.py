# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
# 2022 3.15

class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        # v1 slow, two pass, stack
        stack=[]
        ret=[]
        l=list(s)
        for item in l:
            if item in ['(',')']:
                if  item=='(':
                    stack.append(item)
                    ret.append(item)
                else:
                    if item==')' and stack and stack[-1]=='(':
                        stack.pop()
                        ret.append(item)
            else:
                ret.append(item)
        if not ret:
            return ''
        # print(stack)
        # print(ret)
        i=1
        while stack:
            if ret[-i]==stack[-1]:
                stack.pop()
                ret.pop(-i)
            else:
                i+=1
        return ''.join(ret)

        # v2 