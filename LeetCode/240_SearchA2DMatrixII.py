# https://leetcode.com/problems/search-a-2d-matrix-ii/
# 2022年05月28日 12:36:45

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # v1 , 200ms
        for item in matrix:
            if item[-1]>=target:
                for subitem in item:
                    if subitem==target:
                        return True
                    elif subitem>target:
                        break
        return False
    
    
        # v1.1, 193ms
        r=len(matrix[0])-1 # right boundary
        for item in matrix:
            if item[r]>=target:
                for idx,subitem in enumerate(item[:r+1]):
                    if subitem==target:
                        return True
                    elif subitem>target:
                        r=idx
                        break
        return False
    
        # v1.2, copied , even slower?
        j = -1
        for row in matrix:
            while j + len(row) and row[j] > target:
                j -= 1
            if row[j] == target:
                return True
        return False

        
        
        # v2 binary search, 200ms
        # 想法：写一个二分查找的函数，然后把纵列最后一列送到函数里，得到在第几行
        # 然后把这一行横向送到函数里，得到新的列，然后把新列送到函数里
        up = 0 # up boundary
        r = len(matrix[0])-1 # left boundary
        while 1:
            vrange = list(map(lambda x: x[r], matrix[up:])) 
            vlocation = bisect.bisect(vrange,target)
            up=up+vlocation
            if matrix[up-1][r] == target:
                return True
            if up>len(matrix)-1:
                return False
            hrange = matrix[up][:r]
            hlocation = bisect.bisect(hrange,target)
            r=min(r-1,hlocation)
            if matrix[up][hlocation-1] == target:
                return True
            if r<0:
                return False
        return False

        # v3 copied, one-liner O(m*n), theoretically slow but actually not very slow in this problem
        # https://leetcode.com/problems/search-a-2d-matrix-ii/discuss/66168/4-lines-C-6-lines-Ruby-7-lines-Python-1-liners
        return any(target in row for row in matrix)