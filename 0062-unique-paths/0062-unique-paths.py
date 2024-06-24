class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1 for j in range(n)] for i in range(m)]
        for ii in range(m):
            for jj in range(n):
                if ii==0 and jj==0:
                    dp[ii][jj]=1
                    continue
                up=0
                left=0
                if ii>0:
                    up=dp[ii-1][jj]
                if jj>0:
                    left=dp[ii][jj-1]
                dp[ii][jj]=up+left
        return dp[m-1][n-1]