# https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/
# 2022年09月09日 16:24:16

class Solution:
    def numberOfWeakCharacters(self, p: List[List[int]]) -> int:
        # v1 copied
        p.sort(key=lambda x:(-x[0],x[1]))
        ret=0
        defenseMax=0
        for c in p:
            if c[1]<defenseMax:
                ret+=1
            else:
                defenseMax=c[1]
        return ret
        
        # p.sort(key=lambda x:(-x[0],-x[1]))
        # print(p)
        # ret=0
        # defenseMax=p[0][1]
        # defenseMaxAttack=p[0][0]
        # lastGroupDefMax=p[0][1]
        # attackMax=p[0][0]
        # for i in range(len(p)):
        #     if p[i][0]==attackMax:
        #         if p[i][1]>defenseMax:
        #             lastGroupDefMax=defenseMax
        #             defenseMax=p[i][1]
        #             defenseMaxAttack=p[i][0]
        #     else:
        #         if p[i][1]<lastGroupDefMax or (p[i][1]<defenseMax and p[i][0]<defenseMaxAttack ):
        #             ret+=1
        #             print(p[i])
        #         if p[i][1]>defenseMax:
        #             lastGroupDefMax=defenseMax
        #             defenseMax=p[i][1]
        #             defenseMaxAttack=p[i][0]
        # return ret
    
        p.sort(key=lambda x:(-x[0],-x[1]))
        # print(p)
        ret=0
        defenseMax=p[0][1]
        defenseMaxAttack=p[0][0]
        lastGroupDefMax=0
        for i in range(len(p)):
            if p[i][1]<lastGroupDefMax or (p[i][1]<defenseMax and p[i][0]<defenseMaxAttack ):
                ret+=1
                # print(p[i])
            if p[i][1]>defenseMax:
                lastGroupDefMax=defenseMax
                defenseMax=p[i][1]
                defenseMaxAttack=p[i][0]
        return ret