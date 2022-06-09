# https://leetcode.com/problems/pascals-triangle/
# 2021 12.17

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # v1
        pascal=[]
        for i in range(1,numRows+1):
            thisline=[1]*i
            if i > 2:
                for j in range(1,i-1):
                    thisline[j]=pascal[i-2][j-1]+pascal[i-2][j]
            pascal.append(thisline)
        return pascal

