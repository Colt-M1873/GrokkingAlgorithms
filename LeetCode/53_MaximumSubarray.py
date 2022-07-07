# https://leetcode.com/problems/maximum-subarray/
# 2021 11.29 2022 3.06 3.09
# Totally no fucking idea
# 2022年07月07日 16:51:51


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:  
        # # v1 copied
        # cur_max=glob_max=nums[0]
        # for i in range(1,len(nums)):
        #     cur_max=max(cur_max+nums[i],nums[i])
        #     glob_max=max(cur_max,glob_max)
        # return glob_max
        
        # v2 copied  DP
        dp=[0]*len(nums)
        for i in range(len(nums)):
            dp[i]=max(dp[i-1]+nums[i],nums[i])
        return max(dp)


        # copied 
        # ref https://leetcode.com/problems/maximum-subarray/discuss/20193/DP-solution-and-some-thoughts
        # learn the thinking pattern within upper link
        # dp is to divide those problems into smaller sub-problems
        # and record answer of each sub-problem, using these answer to solve original problem
        dp=[nums[0]]
        for _, val in enumerate(nums[1:]):
            dp.append(max(dp[-1]+val,val))
        return max(dp)


        # copied, Kadane's algorithm, legendary
        # https://leetcode.com/problems/maximum-subarray/discuss/20396/Easy-Python-Way
        # https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)

        # simpler version
        for i in range(1,len(nums)):
            nums[i] = max(nums[i], nums[i-1] + nums[i])
        return max(nums)



        # using builtin accumulate
        # https://leetcode.com/problems/maximum-subarray/discuss/293206/Python-One-liner-using-itertools-(beating-99.70-)
        from itertools import accumulate
        return max(accumulate(nums, lambda x, y: max(y, x+y) ))
