# https://leetcode.cn/problems/unique-paths/description/
# 2022年10月18日 18:34:13

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 每个格子的路径数等于其右侧和下方的格子的路径数的和
        # 终点左侧一格的路径为1，上方一格的路径为1，左上方一格的路径为1+1=2
        # 同理，最后一行的路径数全是1，因为只有右侧，没有下方的格子
        # 同理，最后一列的路径数全是1，因为只有下方，没有右侧的格子
        # 然后重复此规律直到回到起点
        # 或者在一开始将终点处格子设置为1，然后对整个网格在下方和右侧进行padding，
        # 然后在起点和终点之间进行 当前格路径数=右侧格+下方格 的计算

        # # v1 先将最后一行和最后一列全填上1，然后区分mn均大于1和不大于1的情况
        # dp=[[0]*n for _ in range(m)]
        # dp[m-1]=[1]*n
        # for i in range(m):
        #     dp[i][n-1]=1
        # # print(dp)
        # if m==1 or n==1:
        #     return dp[0][0]
        # # m,n均大于1的情况
        # for i in range(m-2,-1,-1):
        #     for j in range(n-2,-1,-1):
        #         dp[i][j]=dp[i+1][j]+dp[i][j+1]
        # return dp[0][0]
        
        # v2 padding，在末尾增加全是0的一行和一列，然后仅把终点下方一格的位置置为1
        # 以便从终点格开始，对从终点到起点的所有格子进行同样的“当前格路径数=右侧格+下方格”的计算
        dp=[[0]*(n+1) for _ in range(m+1)]
        dp[m][n-1]=1 # 终点下方一格，这样做会让终点格值为1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                dp[i][j]=dp[i+1][j]+dp[i][j+1]
        return dp[0][0]