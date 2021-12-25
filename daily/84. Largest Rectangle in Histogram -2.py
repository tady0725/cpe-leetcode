from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        # i => index , h => height
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:  # 當前一個數字大於表示無法往後延伸
                # print(stack[-1][1])
                index, height = stack.pop()  # 存下 起始index &h
                maxArea = max(maxArea, height*(i-index))
                start = index  # 移至新的索引
            stack.append((start, h))
        for i, h in stack:
            maxArea = max(maxArea, h*(len(heights)-i))
        return maxArea


heights = [2, 1, 5, 6, 2, 3]
print(Solution().largestRectangleArea(heights))
