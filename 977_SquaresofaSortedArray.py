# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # # v1  bravo, my first oneliner
        # return [x**2 for x in sorted([abs(x) for x in nums])]
        
        # # v1.1 copied  better oneliner, abs() is redundant
        # return sorted(x**2 for x in nums)
        
        # v2 copied  elegant approach using deuqe
        answer = collections.deque()
        l, r = 0, len(nums) - 1
        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])
            if left > right:
                answer.appendleft(left * left)
                l += 1
            else:
                answer.appendleft(right * right)
                r -= 1
        return list(answer)
        
        # # v2.1  like v2 but without deque
        # answer = [0] * len(nums)
        # l, r = 0, len(nums) - 1
        # while l <= r:
        #     left, right = abs(nums[l]), abs(nums[r])
        #     if left > right:
        #         answer[r - l] = left * left
        #         l += 1
        #     else:
        #         answer[r - l] = right * right
        #         r -= 1
        # return answer       
        
        
        # # v2.2 copied
        # answer = [] # list
        # l, r = 0, len(nums) - 1
        # while l <= r:
        #     left, right = abs(nums[l]), abs(nums[r])
        #     if left > right:
        #         answer.append(left * left)
        #         l += 1
        #     else:
        #         answer.append(right * right)
        #         r -= 1
        # return (answer[::-1]) # reverse list using step of -1 [::-1]
