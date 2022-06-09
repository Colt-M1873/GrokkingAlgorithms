# https://leetcode.com/problems/container-with-most-water/
# 2022年04月05日 14:34:27

# same as 42 trapping rain water

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # # v1 failed, too slow
        # ret=0
        # for i in range(len(height)):
        #     for j in range(i+1,len(height)):
        #         currv=(j-i)*min(height[i],height[j])
        #         if currv>ret:   
        #             ret=currv
        # return ret
        
        # v2 copied, two pointer
        # https://leetcode.com/problems/container-with-most-water/discuss/6100/Simple-and-clear-proofexplanation
        # while diminishing the distance between left and right pointer
        # there are only one case which can enlarge the volume
        # that is enlarge the height of the shorter one 
        l,r=0,len(height)-1
        vmax=0
        while l<r:
            currv=min(height[l],height[r])*(r-l)
            if currv>vmax:
                vmax=currv
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return vmax
       