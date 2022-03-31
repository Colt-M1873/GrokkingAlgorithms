# https://leetcode.com/problems/search-a-2d-matrix/
# 2022 3.30

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # # v1 traverse search, slow
        # for item in matrix:
        #     if target>=item[0] and target<=item[-1]:
        #         for subitem in item:
        #             if subitem==target:
        #                 return True
        #         break
        # return False
    
        # v2 binary search,faster
        # Search rows
        low=0
        high=len(matrix)
        while low<high:
            mid=(low+high)//2
            # print(mid)
            if matrix[mid][-1]<target:
                low=mid+1
            elif matrix[mid][0]>target:
                high=mid
            else:
                break
        # Search within row
        newlow=0
        newhigh=len(matrix[0])
        while newlow<newhigh:
            newmid=(newlow+newhigh)//2
            # print(newmid)
            if matrix[mid][newmid]==target:
                return True
            elif matrix[mid][newmid]<target:
                newlow=newmid+1
            else:
                newhigh=newmid
        return False


        # v3 copied, binary search by flattening the matrix into an array
        if not matrix or not matrix[0]: return False
        m, n = len(matrix[0]), len(matrix)
        beg, end = 0, m*n - 1
        while beg < end:
            mid = (beg + end)//2
            if matrix[mid//m][mid%m] < target:
                beg = mid + 1
            else:
                end = mid
        return matrix[beg//m][beg%m] == target