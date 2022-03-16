# https://leetcode.com/problems/merge-sorted-array/
# 2021 12.07
class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # # v1 oneliner builtin modules used
        # nums1[:]=sorted(nums1[:m]+nums2[:n])
        
        # # v2  cheating, not in-place but passed
        # out=[]
        # a=nums1[:m]
        # b=nums2[:n]
        # while a and b:
        #     if a[0]<b[0]:
        #         out.append(a.pop(0))
        #     elif a[0]==b[0]:
        #         out.append(a.pop(0))
        #         out.append(b.pop(0))
        #     else:
        #         out.append(b.pop(0))
        # out+=a
        # out+=b
        # nums1[:]=out
        # return out

        # v3 list append and bubble sort
        nums1[m:]=nums2[:n]
        for i in range(m+n):
            for j in range(i+1,m+n):
                if nums1[i]>nums1[j]:
                    nums1[i],nums1[j]=nums1[j],nums1[i]
        return nums1

        # v4 two pointer to be finisied

        
        


# s=Solution()
# a=[1,2,3,0,0,0]
# m=0
# b=[2,5,6]
# n=3
# print(s.merge(a,m,b,n))