# https://leetcode.com/problems/combinations/
# 2022年07月11日 14:18:26

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # sub-problem of permutation
        # v1 copied 
        # https://leetcode.com/problems/combinations/discuss/26990/Python-easy-to-understand-DFS-solution
        ret=[]
        nums=list(range(1,n+1))
        def recursion(nums,k,path,ret):
            if len(path)==k:
                ret.append(path)
                return
            for i in range(len(nums)):
                recursion(nums[i+1:],k,path+[nums[i]],ret)
        recursion(nums,k,[],ret)
        return ret
        

# iterative backtracking
# https://leetcode.com/problems/combinations/discuss/27029/AC-Python-backtracking-iterative-solution-60-ms