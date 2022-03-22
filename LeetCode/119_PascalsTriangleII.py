# https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # # v1 modified Q118
        # pascal=[]
        # for i in range(1,rowIndex+2):
        #     thisline=[1]*i
        #     if i > 2:
        #         for j in range(1,i-1):
        #             thisline[j]=pascal[i-2][j-1]+pascal[i-2][j]
        #     pascal.append(thisline)
        # return pascal[rowIndex]

        # v2 by the difinition of Pascal Triangle
        # Say we have the current layer [1, 2, 1]. 
        # We then make 2 copies of this layer, 
        # add 0 to the start of one copy, and add 0 to the end of one copy; 
        # then we have [0, 1, 2, 1] and [1, 2, 1, 0]. 
        # Then we can perform the element-wise add operation and we would have [1, 3, 3, 1]. This is from the definition of Pascal's Triangle.
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row