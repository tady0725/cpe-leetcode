import math
'''
先求出 a, b 的最小公倍數 lcm(a, b) = a * b / gcd(a, b), 其中 gcd 表示最大公約數
由韋恩圖可知 f(x) = x / a + x / b - x / lcm(a, b)
即找出 x / a + x / b - x / lcm(a, b) >= n 的最小 x
那麼可以嘗試採用二分查找, 找到 n 個滿足能整除 a 或 b 的數
下界取 0, 上界取 n * max(a, b) = 10 ^ 15
時間複雜度爲 O(lg(n * max(a, b))), 空間複雜度爲 O(1)
'''


class Solution:
    def nthMagicalNumber(self, N, A, B):
        lcm, Q = A*B//math.gcd(A, B), 1_000_000_007  # 10^9 + 7

        beg, end = 0, N * min(A, B)
        while beg < end:
            mid = (beg + end)//2
            if mid//A + mid//B - mid//lcm < N:
                beg = mid + 1
            else:
                end = mid

        return beg % Q


n, a, b = 5, 2, 4
print(Solution().nthMagicalNumber(n, a, b))
'''
Input: n = 4, a = 2, b = 3
Output: 6

2 3 4 6  8 9 10 
'''

''' time Limit 
    def nthMagicalNumber(self, N, A, B):
        s = []
        count = 0
        for i in range(1, 1_000_000_007):
            if i % A == 0:
                if i not in s:
                    s.append(i)
                    count += 1
            elif i % B == 0:
                if i not in s:
                    s.append(i)
                    count += 1
            if count > N:
                return s[N-1]
        
'''
