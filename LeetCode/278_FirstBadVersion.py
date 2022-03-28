# https://leetcode.com/problems/first-bad-version/
# 2021 11.20


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):
#     return

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # v1
        left,right=1,n
        if n==1:
            return 1
        while left<=right:
            pivot=(left+right)//2
            if isBadVersion(pivot):
                lastpivot=pivot
                right=pivot-1
            else:
                left=pivot+1
        return lastpivot

        # # v2
        # left,right=1,n
        # if n==1:
        #     return 1
        # while left<=right:
        #     pivot=(left+right)//2
        #     if isBadVersion(pivot):
        #         # lastpivot=pivot
        #         right=pivot-1
        #         if not isBadVersion(right):
        #             return pivot
        #     else:
        #         left=pivot+1
        # return pivot