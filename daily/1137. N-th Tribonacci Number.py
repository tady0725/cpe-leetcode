class Solution:
    def tribonacci(self, n: int) -> int:
        t = {}
        t[0] = 0
        t[1] = 1
        t[2] = 1
        for i in range(3, n+1):
            t[i] = t[i-3] + t[i-2] + t[i-1]

        return t[n]


n = 25
print(Solution().tribonacci(n))

'''T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
'''
