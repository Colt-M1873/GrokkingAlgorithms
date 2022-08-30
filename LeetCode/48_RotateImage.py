# https://leetcode.com/problems/rotate-image/submissions/
# 2022年08月30日 15:08:16


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # v1 copied, oneliner
        # https://leetcode.com/problems/rotate-image/discuss/18884/Seven-Short-Solutions-(1-to-7-lines)
        matrix[:]=zip(*matrix[::-1])