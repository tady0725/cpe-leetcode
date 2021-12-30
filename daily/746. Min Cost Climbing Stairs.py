from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

    # 1. initialize dp table with length
        dp = [0] * (n + 2)

    # dp function , transfer condition

    # 3. base condition , f(0) = 0, f(1) = 1, f(2) = 2
        dp[0] = 0
        dp[1] = 0
        # dp[2] = min  dp[0] + cost[0], dp[1] + cost[1] = 10
        # dp[3] = min  dp[2] + cost[2], dp[1] + cost[1] = 15
        # dp[4] = min  dp[3] + cost[3], dp[2] + cost[2]
        # dp[5] = min  dp[4] + cost[4], dp[3] + cost[3]

    # 4. transfer condition  - range -> [2,n+1) -> ==[2,n]  , find the transfer fountion came from below
        for i in range(2, n + 1):
            # 一次走一步或兩步 選擇花費較低的成本
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

    # 5. end/ return condition
    # # last one is 'last index + 1', means you jump out the stairs
        return dp[n]


cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(Solution().minCostClimbingStairs(cost))
