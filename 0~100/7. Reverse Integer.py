class Solution:
    def reverse(self, x: int) -> int:
        s = str(abs(x))
        # string reverse to int
        reversed = int(s[::-1])
        # out of range
        if reversed > 2**31:
            return 0
        # negative number
        return reversed if x > 0 else (reversed * -1)


x = 2111
print(Solution().reverse(x))
