# https://leetcode.com/problems/merge-sorted-array/
# 2021 12.07 2022 3.20 3.21

class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # # v1 oneliner using builtin sort and slice assignment
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

        # 2022 3.21
        # v4 two pointer copied,one pass, super fast
        # https://leetcode.com/problems/merge-sorted-array/discuss/29503/Beautiful-Python-Solution
        # 因为大头全是0，所以可以双指针从大到小排列而不损失nums1中的信息
        while m>0 and n>0:
            if nums1[m-1]>nums2[n-1]:
                nums1[m+n-1]=nums1[m-1]
                m-=1
            else:
                nums1[m+n-1]=nums2[n-1]
                n-=1
        if n>0:
            nums1[:n]=nums2[:n]
        
        # 2022年06月07日 10:21:53  
        # 31min 
        # ugly version of v4
        # backward, from big to small, swap and fill the empty zerr
        # m and n as pointer
        m-=1
        n-=1
        for i in range(len(nums1)-1,-1,-1):
            if m>=0 and n>=0:
                if nums1[m]>=nums2[n]:
                    nums1[i],nums1[m] = nums1[m],nums1[i]
                    m-=1
                elif nums1[m]<nums2[n]:
                    nums1[i]=nums2[n]
                    n-=1
            elif m>=0 and n<0:
                nums1[i],nums1[m] = nums1[m],nums1[i]
                m-=1
            elif m<0 and n>=0:
                nums1[i]=nums2[n]
                n-=1
     