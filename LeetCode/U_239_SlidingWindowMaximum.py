# https://leetcode.com/problems/sliding-window-maximum/
# 2022年07月07日 15:43:42

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # v1 copied monotonic dequeue
        # https://leetcode.com/problems/sliding-window-maximum/discuss/871317/Clear-thinking-process-with-PICTURE-brute-force-to-mono-deque-pythonjavajavascript
        from collections import deque
        q=deque()
        ret=[]
        for idx, curr in enumerate(nums):
            while q and curr >= nums[q[-1]]:
                q.pop()
            q.append(idx)
            if q[0]==idx-k:
                q.popleft()
            if idx >= k-1:
                ret.append(nums[q[0]])
        return ret