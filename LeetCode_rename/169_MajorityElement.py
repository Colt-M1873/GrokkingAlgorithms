# https://leetcode.com/problems/majority-element/
# 2022年04月17日 15:10:20

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # # v1  iterative using dict
        # d={}
        # for item in nums:
        #     if item not in d:
        #         d[item]=1
        #     else:
        #         d[item]+=1
        # maxitem=nums[0]
        # for item in d.keys():
        #     if d[item]>d[maxitem]:
        #         maxitem=item
        # return maxitem
    
        # # v2 copied, 
        # # NOTICE that the majority element always exist in the array,so that the middle always is the answer
        # return sorted(nums)[len(nums)/2]
        
        # v3 copied, Boyer-Moore Majority Vote Algorithm
        # 摩尔投票算法 https://www.zhihu.com/question/49973163/answer/235921864
        # 相当于分出了正负两类，投票，并且正负票数相抵消，剩下的最后一个就是majority element
        # 并且还用到了DP的思想
        major=nums[0]
        count=1
        for i in range(1,len(nums)):
            if count!=0:  # DP，动态的记录在当前这一段里面的票数，如果归零了，就证明当前这一段里面不存在majority element，重新计算
                if nums[i]==major: # 相同则加一票
                    count+=1
                elif nums[i]!=major: # 发现不同则减一票
                    count-=1
            else:
                count+=1
                major=nums[i]
        return major
            
        # https://leetcode.com/problems/majority-element/discuss/51613/O(n)-time-O(1)-space-fastest-solution   
        # major=nums[0]
        # count=1
        # for i in range(len(nums)):
        #     if count==0:
        #         count+=1
        #         major=nums[i]
        #     elif major==nums[i]:
        #         count+=1
        #     else:
        #         count-=1
        # return major