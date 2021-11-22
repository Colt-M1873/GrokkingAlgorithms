class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # v1  bravo, my first oneliner
        return [x**2 for x in sorted([abs(x) for x in nums])]
        
        # v2
        
        
        