# https://leetcode.com/problems/permutations/
# 2022年07月11日 13:37:16

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # v1 copied recursion backtracking, slow
        # recording paths while recursvely DFS traversing a tree
        # https://leetcode.com/problems/permutations/discuss/18296/Simple-Python-solution-(DFS).
        ret=[]
        def backtracking(nums,path,ret):
            if not nums: ret.append(path)
            for i in range(len(nums)):
                backtracking(nums[:i]+nums[i+1:],path+[nums[i]],ret)
        backtracking(nums,[],ret)
        return ret
        # v2 oneliners
        # https://leetcode.com/problems/permutations/discuss/18241/One-Liners-in-Python



        # general approach for backtracking
        # https://leetcode.com/problems/permutations/discuss/18239/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partioning)


        # illustration and complexity analysis
        # https://leetcode.com/problems/permutations/discuss/993970/Python-4-Approaches-%3A-Visuals-%2B-Time-Complexity-Analysis

        # faster approaches needed