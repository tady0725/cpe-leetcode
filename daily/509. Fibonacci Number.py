class Solution:
    def fib(self, n: int) -> int:
        fib = {}
        # 向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值
        fib[0] = 0
        fib[1] = 1
        for i in range(2, n+1):
            fib[i] = fib[i-1]+fib[i-2]

        return fib[n]


n = 10
print(Solution().fib(n))
'''class Solution(object):
    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)'''
