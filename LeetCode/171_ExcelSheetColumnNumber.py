# https://leetcode.com/problems/excel-sheet-column-number/
# 2022年04月17日 21:12:46

class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        # # v1 change from base 10 to base 26
        # s=0
        # for i in range(len(columnTitle)):
        #     thisord=ord(columnTitle[i])-ord('A')+1
        #     s=s*26+thisord
        # return s
        
        # # v1.1
        # s=0
        # for i in range(len(columnTitle)):
        #     s=s*26+ord(columnTitle[i])-ord('A')+1
        # return s
        
        # v2 recursive oneliner
        return 0 if not columnTitle else (ord(columnTitle[-1])-ord('A')+1)+26*(self.titleToNumber(columnTitle[:-1]))
        