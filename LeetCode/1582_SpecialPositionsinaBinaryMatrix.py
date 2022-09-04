# https://leetcode.cn/problems/special-positions-in-a-binary-matrix/
# 2022年09月04日 19:59:36

# v1 
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        sr=[]
        sc=0
        for idx,r in enumerate(mat) :
            if sum(r)==1:
                for i,val in enumerate(r):
                    if val==1:
                        sr.append(i)
                
        for i in sr:
            col=list(map(lambda x:x[i],mat))
            if sum(col)==1:
                sc+=1
        return sc



# v2 copied, simple and fast using zip
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        sr=[sum(r) for r in mat]
        sc=[sum(c) for c in zip(*mat)]
        return sum(mat[i][j]==1 and sr[i]==1 and sc[j]==1 for i in range(len(mat)) for j in range(len(mat[0])))
        