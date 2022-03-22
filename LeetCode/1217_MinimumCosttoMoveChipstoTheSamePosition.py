# https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # v2 most important thing is to find pattern, to get keypoint
        # even to even cost 0 odd to odd cost 0, even to odd cost 1
        # so the minimum cost is the smaller one between even and odd
        even=0
        odd=0
        for i in range(len(position)):
            if position[i]%2==1:
                odd+=1
            else:
                even+=1
        return min(even,odd)
    
        # # v2.1 copied oneliner
        # return min(len([i for i in position if i%2==0]), len([i for i in position if i%2==1]))  
        
        
        # # v2.2 copied use collection.counter
        # d = collections.Counter([c % 2 for c in position])
        # return min(d[0], d[1])
        
        
        # # v1 dumb and wrong answer, not getting the keypoint
        # mostoccuredlist=[position[0]]
        # mostoccuredcount=1
        # thisoccuredcount=1
        # position=sorted(position)
        # for i in range(1,len(position)):
        #     if position[i]==position[i-1]:
        #         thisoccuredcount+=1
        #     else:
        #         thisoccuredcount=1
        #     if thisoccuredcount>mostoccuredcount:
        #         mostoccuredcount=thisoccuredcount
        #         mostoccuredlist=[position[i]]
        #     elif thisoccuredcount==mostoccuredcount:
        #         mostoccuredlist.append(position[i])
        # retlist=[0]*len(mostoccuredlist)
        # for k in range(len(mostoccuredlist)):
        #     for j in range(len(position)):
        #         if (position[j]-mostoccuredlist[k])%2==1:
        #             retlist[k]+=1
        # return min(retlist)