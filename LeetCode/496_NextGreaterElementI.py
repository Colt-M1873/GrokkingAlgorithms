# https://leetcode.com/problems/next-greater-element-i/
# 2022年05月26日 11:37:52

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # # v1 hashtable  O(n^2)
        # ret=[]
        # d={}
        # nums2.append(-1)
        # for idx,item in enumerate(nums2):
        #     j=min(idx+1,len(nums2)-1)
        #     while j<len(nums2)-1 and item>nums2[j] :
        #         j+=1
        #     d[item]=nums2[j]
        # for item in nums1:
        #     ret.append(d[item])
        # return ret
    
        # v2 copied, monotonic stack + hashtable O(n)
        # https://leetcode.com/problems/next-greater-element-i/discuss/97604/Python-Solution-with-O(n) 
        # 这是一个单调递减栈，如果碰到了比栈顶还大的数就不断出栈
        # 很费脑子，这里的大致意思是：
        # 循环获取nums2里的数，每个数都进一遍栈，并且维持栈里从大到小的顺序，
        # 如果当前的数比栈顶大，就pop出栈直到栈空或者直到栈顶比当前数更大
        # pop出的这部份数的next greater element是当前数
        d={}
        ret=[]
        mstack=[]
        for item in nums2:
            while mstack and mstack[-1]<item:
                prev_num=mstack.pop()
                d[prev_num]=item
            mstack.append(item)
        for item in nums1:
            ret.append(d.get(item,-1))
        return ret
    
        # labuladong书里的方法是从后向前取数，可以重写一下
        
         
        # # v3 oneliner but O(m*n) StefanPochmann
        # # https://leetcode.com/problems/next-greater-element-i/discuss/97616/Meh-1000-is-small
        #  return [next((y for y in nums2[nums2.index(x):] if y > x), -1) for x in nums1]
    