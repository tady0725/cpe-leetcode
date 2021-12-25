class Solution:
    def maxPower(self, s: str) -> int:
        longest = 0
        tmp = 1
        for i in range(len(s)):
            if i+1 < len(s) and s[i] == s[i+1]:
                tmp += 1
            else:
                tmp = 1
            longest = max(longest, tmp)
        return longest


s = "abbcccddddeeeeedcba"
print(Solution().maxPower(s))
'''
        count = 0
        max_count = 0
        pre = ""
        for c in s:
            if c == pre:
                count += 1
            else:
                pre = c
                count = 1
            max_count = max(max_count, count)
        return max_count

'''
