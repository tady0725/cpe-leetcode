class Solution:
    def numTilings(self, n):
        dp = [[0, 0] for _ in range(n+2)]
        dp[1], dp[2] = [1, 1], [2, 2]
        for i in range(3, n+1):
            dp[i][0] = dp[i-1][0] + dp[i-2][0] + 2*dp[i-2][1]
            dp[i][1] = dp[i-1][0] + dp[i-1][1]
        return dp[n][0] % 1_000_000_007  # 10^9 + 7


n = 3
print(Solution().numTilings(n))
'''
dp[n]=dp[n-1]+dp[n-2]+2*(dp[n-3]+...+d[0])
=dp[n-1]+dp[n- 2]+dp[n-3]+dp[n-3]+2*(dp[n-4]+...+d[0])
=dp[n-1]+dp[n-3] +(dp[n-2]+dp[n-3]+2*(dp[n-4]+...+d[0]))
=dp[n-1]+dp[n-3] +dp[n-1]
=2*dp[n-1]+dp[n-3]

https://www.youtube.com/watch?v=S-fUTfqrdq8
'''
