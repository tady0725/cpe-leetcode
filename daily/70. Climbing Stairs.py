'''
第一 : 1 (1)
第二 : 2 (1+1 , 2)
第三 : 3 (1+1+1 , 2+1 , 1+2)
第四 : 5  (1+1+1+1 , 2+1+1 , 1+2+1 , 1+1+2 , 2+2)
前一個 +1 ，前兩個加 +2 就等於下個總
'''


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1]+dp[i-2]

        return dp[n]


n = 6
print(Solution().climbStairs(n))
