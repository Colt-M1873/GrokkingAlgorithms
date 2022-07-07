# https://leetcode.com/problems/zigzag-conversion/
# 2022年07月06日 22:30:43

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # v1  actually build a matrix, draw and read the pattern
        if len(s)<=numRows or numRows==1: return s
        s=list(s)
        mat=[]
        ret=''
        for i in range(len(s)):
            if i%(2*numRows-2)==0:
                mat.append(s[i:i+numRows])   
                for j in range(0,numRows-2):
                    curr=[None]*numRows
                    if i+numRows+j>=len(s):
                        break
                    curr[-(j+2)]=s[i+numRows+j]
                    mat.append(curr)
        if len(mat[-1]) != numRows:
            mat[-1]+=[None]*(numRows-len(mat[-1]))
        # print(mat) 
        for i in range(numRows):
            for j in range(len(mat)):
                if mat[j][i]:
                    ret+=mat[j][i]
        return ret
        
        # v2 cpoied, finding the pattern
        # https://leetcode.com/problems/zigzag-conversion/discuss/817306/Very-simple-and-intuitive-O(n)-python-solution-with-explanation
        if numRows>=len(s) or numRows==1:return s
        L=[]
        linenum=0
        direction=1  # 1 for up, -1 for down
        for i in range(len(s)):
            if linenum==numRows:
                direction=-1
            if linenum==1:
                direction=1
            linenum+=direction
            L.append((s[i],linenum))
        strlist=['']*numRows
        for item in L:
            strlist[item[1]-1]+=item[0]
        # print(strlist)
        return ''.join(strlist)