
class Solution:
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        elif n == 1:
            return True
        while n % 2 == 0:
            n /= 2
            if n == 1:
                return True


n = 1000
print(Solution().isPowerOfTwo(n))
