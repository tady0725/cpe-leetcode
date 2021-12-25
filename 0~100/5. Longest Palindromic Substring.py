
class Solution:

    def longestPalindrome(self, s):
        res = ""
        reslen = 0
        for i in range(len(s)):
            # odd len
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if(r-l + 1) > reslen:
                    res = s[l:r+1]

                    reslen = r-l+1
                l -= 1
                r += 1  # 以中心往左右
                # print(i)
                # print(l, r)
                # print(res)
            # even len
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if(r-l + 1) > reslen:
                    res = s[l:r+1]
                    reslen = r-l+1
                l -= 1
                r += 1
        return res


'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 1.先判斷該字串是否為一個字母，或是本身是迴文
        if (len(s) <= 1) or s == s[::-1]:
            return s
        else:
            # 紀錄開始的位置
            startIndex = 1
            # 紀錄目前最大迴文的長度
            maxLen = 1
            # 開始跑迴圈
            for i in range(1, len(s)):
                # 跑第一圈時，odd要找 s[-1:2]，event要找 s[0:2]
                # 跑第二圈時，odd要找 s[0:3]，event要找 s[1:3]
                # 跑第三圈時，odd要找 s[1:4]，event要找 s[2:4]
                odd = s[i - maxLen - 1: i + 1]
                print(odd)
                even = s[i - maxLen: i + 1]
                print(even)
                # 判斷odd是否為迴文
                if i - maxLen - 1 >= 0 and odd == odd[::-1]:
                    startIndex = i - maxLen - 1
                    maxLen += 2
                elif i - maxLen >= 0 and even == even[::-1]:
                    startIndex = i - maxLen
                    maxLen += 1
        return s[startIndex: startIndex + maxLen]
'''

s = "vvabcba"
print(Solution().longestPalindrome(s))
