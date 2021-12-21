# https://leetcode.com/problems/minimum-absolute-difference/

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # v1 too slow excedded time limit
        arr=sorted(arr)
        minDiff=abs(arr[0]-arr[1])
        ret=[]
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                Diff=abs(arr[j]-arr[i])
                if Diff<minDiff:
                    minDiff=Diff
                    ret=[[arr[i],arr[j]]]
                elif Diff==minDiff:
                    ret.append([arr[i],arr[j]])
        return ret