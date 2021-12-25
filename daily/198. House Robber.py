from typing import List
from functools import lru_cache


class Solution:
    def rob(self, nums: List[int]) -> int:

        prev2, prev, cur = 0, 0, 0
        for i in nums:
            cur = max(prev, i + prev2)  # 不能相鄰找出前前一筆最大
            prev2 = prev  # 往右移
            prev = cur  # 當前最大

        return cur


nums = [1, 2, 3, 1]
print(Solution().rob(nums))
