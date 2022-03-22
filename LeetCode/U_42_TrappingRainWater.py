# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        
        left_max=[0]*len(height)
        right_max=[0]*len(height)
        left_max[0]=height[0]
        right_max[-1]=height[-1]
        for i in range(1,len(height)):
            if height[i] >left_max[i-1]:
                left_max[i]=height
            else:
                left_max[i]=left_max[i-1]
            if height[-i-1]>right_max[-i-1]:
                right_max[-i-1]=height[-i-1]
            else:
                right_max[-i-1]=right_max[-i]

        print(left_max)
        print(right_max)
        result=0
        for i in range(len(height)):
            result+=min(left_max[i],right_max[i])-height[i]
        
        return result
