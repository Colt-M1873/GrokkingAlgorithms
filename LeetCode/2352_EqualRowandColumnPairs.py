# https://leetcode.com/problems/equal-row-and-column-pairs/
# 2022年07月25日 14:28:10

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # # V1 BUILDING A TRASNPOSE MATRIX, slow 1200ms
        # transpose=[]
        # ret=0
        # for i in range(len(grid[0])):
        #     transpose.append(list(map(lambda x:x[i],grid)))
        # # print(transpose)
        # for i in range(len(grid)):
        #     for j in range(len(transpose)):
        #         if transpose[j][0]==grid[i][0]:
        #             if transpose[j]==grid[i]:
        #                 ret+=1
        # return ret
    
        # # V1.1 slower 7971ms
        # # no need to build transpose matrix, but need to calculate list(map()) multiple times
        # ret=0
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][0]==grid[0][j]:
        #             if grid[i]==list(map(lambda x:x[j], grid)):
        #                 ret+=1
        # return ret
        
        # # v1.2 1200ms
        # ret=0
        # dCol={} # dict rememberring column index and column itself
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][0]==grid[0][j]:
        #             if j not in dCol:
        #                 dCol[j]=list(map(lambda x:x[j], grid))
        #             if grid[i]==dCol[j]:
        #                 ret+=1
        # return ret
        
        
        # v2 fast, 750ms, beat 100%
        # hash the array and comparing hashes
        # print(hash(grid[0])) # failed, list is mutable so cannot be hashed 
        # print(hash(tuple(grid[0])))
        rowHash,colHash=[],[]
        ret=0
        for i in range(len(grid)):
            rowHash.append(hash(tuple(grid[i])))
            colHash.append(hash(tuple(map(lambda x:x[i], grid))))
        for r,hr in enumerate(rowHash):
            for c,hc in enumerate(colHash):
                if hr==hc:
                    ret+=1
        return ret