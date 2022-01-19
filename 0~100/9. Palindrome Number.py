class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        f = s[::-1]
        if s == f:
            return True
        else:
            return False


x = -121
print(Solution().isPalindrome(x))
