#  Brute Force
# Time complexity : O(n^3)
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        all = []
        for i in range(len(s)):
            record = ""
            record += s[i]
            for j in range(i+1, len(s)):
                if s[j] not in record:
                    record += (s[j])
                else:
                    break
            all.append(len(record))
        # print(max(all))
        return max(all, default=1)
'''

'''
class Solution:
    def lengthOfLongestSubstring(self, s):
        sub_str = ''
        max_len = 0
        for w in s:
            while w in sub_str:
                sub_str = sub_str[1:]
                # print(sub_str)
            else:
                sub_str += w
                max_len = max(len(sub_str), max_len)
        return max_len

'''


class Solution:
    def lengthOfLongestSubstring(self, s):
        all = set()
        l = 0
        res = 0
        for r in range(len(s)):  # 從左至右
            while s[r] in all:
                all.remove(s[l])  # 移除相同字
                l += 1  # 左邊指標往右移
            all.add(s[r])
            res = max(res, r-l+1)  # 較大替換
            print(res)
            # print(all)
        return res


s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))
