# https://leetcode.com/problems/kth-largest-element-in-an-array/
# 2022年05月08日 13:04:23

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # # v1 oneliner built-in method, 105ms, 14.7MB
        # return sorted(nums,reverse=True)[k-1]
        
        # # v2 recursive quick sort, too slow and too much memory wasted
        # # 4896ms, 124MB
        # def quick(n):
        #     if len(n)<=1: return n
        #     pivot=n[0]
        #     smaller=[]
        #     bigger=[]
        #     for item in n[1:]:
        #         if item<pivot:
        #             smaller.append(item)
        #         else:
        #             bigger.append(item)
        #     # print(smaller,"sdadsa",bigger)
        #     return quick(bigger)+[pivot]+quick(smaller)
        # return quick(nums)[k-1]
        
        
        # v2.1 iterative quick sort, slow but relatively space-saving, 3450ms, 20mb
        # 挖坑填数  https://www.runoob.com/w3cnote/quick-sort.html
        def quick_sort_ite(n,l,r):
            if l>r: return []
            p=n[l]
            i,j=l,r
            while i<j:
                while i<j and n[j]>=p:
                    j-=1
                if i<j:
                    n[i]=n[j] # 这一步为什么
                    i+=1
                while i<j and n[i]<p:
                    i+=1
                if i<j:
                    n[j]=n[i] # 这一步为什么
                    j-=1
            n[i] = p
            quick_sort_ite(n,l,i-1)
            quick_sort_ite(n,i+1,r)
            return n
        
        return quick_sort_ite(nums,0,len(nums)-1)[-k]
        
        
        # v2.2 quick select sort
        
        
        
        # v3 heap sort