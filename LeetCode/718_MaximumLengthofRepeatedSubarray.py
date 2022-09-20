# https://leetcode.com/problems/maximum-length-of-repeated-subarray/
# 2022年09月20日 17:15:49

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # # v0 false method of dp, failed , TLE
        # # cause u are using dp array to memorizing all the possible space
        # # u dont need to calculate each length in each point
        # dp=[[0]*len(nums2) for i in range(len(nums1))]
        # for i in range(len(dp)):
        #     for j in range(len(dp[i])):
        #         idx1,idx2=i,j
        #         while idx1<len(nums1) and idx2<len(nums2) and nums1[idx1]==nums2[idx2]:
        #             dp[i][j]+=1
        #             idx1+=1
        #             idx2+=1
        # # print('-'*100)
        # # print(len(nums1),len(nums2))
        # # for d in dp:
        # #     print(d)
        # return max(max(d) for d in dp)
        
        
        # # v0.1 also TLE
        # # reduced search space by recording the place of each number with dict, 
        # # because 0 <= nums1[i], nums2[i] <= 100
        # d=collections.defaultdict(list)
        # for idx,n in enumerate(nums2):
        #     d[n].append(idx)
        # currmax=0
        # for i in range(len(nums1)):
        #     for j in d[nums1[i]]:
        #         idx1,idx2=i,j
        #         if len(nums2)-j<=currmax or len(nums1)-i<=currmax:
        #             continue
        #         length=0
        #         while idx1<len(nums1) and idx2<len(nums2) and nums1[idx1]==nums2[idx2]:
        #             length+=1
        #             idx1+=1
        #             idx2+=1
        #         currmax=max(currmax,length)
        # return currmax
        
        # v1 correct dp memorizing, slow, 7122ms
        memo=[[0]*len(nums2) for _ in range(len(nums1))]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    if i==0 or j==0:
                        memo[i][j]=1
                    else:
                        memo[i][j]=memo[i-1][j-1]+1
        return max(max(m) for m in memo)
                        
              
        