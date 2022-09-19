# https://leetcode.cn/problems/sort-array-by-increasing-frequency/
# 2022年09月19日 20:09:05

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # v1 dumb
        d={}
        for n in nums:
            if n not in d:
                d[n]=1
            else:
                d[n]+=1
        ln=[]
        for item in d:
            ln.append((item,d[item]))
        ln.sort(key=lambda x:(x[1],-x[0]))
        ret=[]
        for x in ln:
            ret+=[x[0]]*x[1]
        return ret


        # v2 copied oneliner
        return sorted(nums, key = lambda n: (nums.count(n), -n) )

        return sorted(nums, key = lru_cache(None)( lambda n: (nums.count(n), -n) ))