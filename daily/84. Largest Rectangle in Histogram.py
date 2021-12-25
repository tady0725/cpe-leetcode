from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        計算直方圖的最大面積
        """

        res = 0
        stack = [-1]  # 較特別，存的是index而不是直接存高度，因為要留存寬度訊息。trick放入index「-1」
        heights.append(0)  # trick: 在陣列尾巴放一個0以把stack內元素拋出
        for i in range(len(heights)):
            # 後方長度較常可往後延伸
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                cur = stack.pop()
                res = max(res, heights[cur] * (i-stack[-1]-1))
            stack.append(i)  # index
        return res
        """時間限制
        # Brute Force
        n = len(heights)
        maxa = 0
        for i in range(n):
            for j in range(i, n):
                h = min(heights[i:j+1])
                # print(heights[i:j+1])
                w = j-i+1
                maxa = max(maxa, h*w)
                # print(maxa)
        return maxa"""


heights = [2, 1, 5, 6, 2, 3]
print(Solution().largestRectangleArea(heights))
