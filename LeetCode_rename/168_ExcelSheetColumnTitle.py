# https://leetcode.com/problems/excel-sheet-column-title/
# 2022年04月17日 12:30:02

class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """

        # # v1 iterative, handleing Z problem separately
        # ret=[]
        # while columnNumber>0:
        #     if columnNumber%26==0: # deal with 'Z'
        #         ret.append('Z')
        #         columnNumber=columnNumber/26-1
        #     else:
        #         ret.append(chr(ord('A')-1+columnNumber%26))
        #         columnNumber=(columnNumber-columnNumber%26)/26
        # return ''.join(ret[::-1])

        # v1.1
        # ret=[]
        # while columnNumber>0:
        #     if columnNumber%26!=0:
        #         thisord=columnNumber%26
        #     else:
        #         thisord=26
        #     ret.append(chr(ord('A')-1+thisord))
        #     columnNumber=(columnNumber-thisord)/26
        # return ''.join(ret[::-1])
        
        # # v1.2 using a new variable to handle the 'Z' problem
        # ret=[]
        # while columnNumber>0:
        #     thisord=columnNumber%26 if columnNumber%26!=0 else 26
        #     ret.append(chr(ord('A')-1+thisord))
        #     columnNumber=(columnNumber-thisord)/26
        # return ''.join(ret[::-1])

        # v2 copied  oneliner
        return "" if columnNumber == 0 else self.convertToTitle((columnNumber - 1) / 26) + chr((columnNumber - 1) % 26 + ord('A'))
