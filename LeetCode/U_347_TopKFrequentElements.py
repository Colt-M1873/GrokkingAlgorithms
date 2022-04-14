# https://leetcode.com/problems/top-k-frequent-elements/
# 2022年04月09日 21:55:27


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # v1 hash table and selection sort
        # traditional dumb solution, relatively slow
        d={}
        ret=[]
        for idx,item in enumerate(nums):
            # print(idx)
            if item in d:
                d[item]+=1
            else:
                d[item]=1
        while len(ret)<k:
            maxkey=d.keys()[0]
            maxval=d[maxkey]
            for key in d.keys():
                if d[key]>maxval:
                    maxval=d[key]
                    maxkey=key
            d.pop(maxkey)
            ret.append(maxkey)
        return ret
            

        # v2 heap 