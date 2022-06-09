# https://leetcode.com/problems/reverse-string/
# 2021 11.25

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # v1  in-place, slice assignment
        s[:]=s[::-1]
        return None
        
        # # v2 copied  two pointer
        # for i in range(len(s)//2): s[i], s[-i-1] = s[-i-1], s[i]
        # return None

        # # v2.1 copied  two pointer with bitwise not ~
        # for i in range(len(s)//2): s[i], s[~i] = s[~i], s[i]
        # return None